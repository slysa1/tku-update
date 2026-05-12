local REPORT_DIR = "D:/Downloads/OneDrive/Documents/code/tku-update/reports/tku_editor_first"
local MAX_PROBES = 40
local PROBE_INTERVAL_MS = 3000
local probes = 0
local wrote_starmap_probe = false

local function now_stamp()
    return os.date("%Y%m%d-%H%M%S")
end

local function report_path(kind)
    return string.format("%s/ue4ss_tku_runtime_probe_%s_%s.txt", REPORT_DIR, kind, now_stamp())
end

local function append_line(handle, text)
    handle:write(tostring(text))
    handle:write("\n")
end

local function safe_call(label, callback)
    local ok, value = pcall(callback)
    if ok then
        return value
    end
    return string.format("<error %s: %s>", label, tostring(value))
end

local function count_table(value)
    if value == nil then
        return 0
    end
    local n = 0
    for _ in pairs(value) do
        n = n + 1
    end
    return n
end

local function object_full_name(value)
    if value == nil then
        return "<nil>"
    end
    return safe_call("GetFullName", function()
        return value:GetFullName()
    end)
end

local function object_path_name(value)
    if value == nil then
        return "<nil>"
    end
    return safe_call("GetPathName", function()
        return value:GetPathName()
    end)
end

local function property_value(object, names)
    if object == nil then
        return "<nil object>"
    end
    for _, name in ipairs(names) do
        local ok, value = pcall(function()
            return object:GetPropertyValue(name)
        end)
        if ok and value ~= nil then
            return value
        end
        ok, value = pcall(function()
            return object[name]
        end)
        if ok and value ~= nil then
            return value
        end
    end
    return "<missing>"
end

local function table_sample_names(objects, limit)
    local out = {}
    if objects == nil then
        return out
    end
    local i = 0
    for _, object in pairs(objects) do
        i = i + 1
        if i <= limit then
            table.insert(out, object_full_name(object))
        end
    end
    return out
end

local function dump_runtime_probe(reason)
    probes = probes + 1

    local bodies = safe_call("FindAllOf StarSystemBody_C", function()
        return FindAllOf("StarSystemBody_C")
    end)
    if type(bodies) ~= "table" then
        bodies = {}
    end

    local pawns = safe_call("FindAllOf StarMapPawn_C", function()
        return FindAllOf("StarMapPawn_C")
    end)
    if type(pawns) ~= "table" then
        pawns = {}
    end

    local actors = safe_call("FindAllOf StarMapActor_C", function()
        return FindAllOf("StarMapActor_C")
    end)
    if type(actors) ~= "table" then
        actors = {}
    end

    local body_count = count_table(bodies)
    local pawn_count = count_table(pawns)
    local actor_count = count_table(actors)
    local kind = "startup"
    if body_count > 100 or pawn_count > 0 or actor_count > 0 then
        kind = "starmap"
        wrote_starmap_probe = true
    end

    local handle = io.open(report_path(kind), "w")
    if handle == nil then
        print("[TKURuntimeProbe] could not open report file\n")
        return
    end

    append_line(handle, "TKU UE4SS Runtime Probe")
    append_line(handle, "generated_local=" .. os.date("%Y-%m-%dT%H:%M:%S%z"))
    append_line(handle, "reason=" .. tostring(reason))
    append_line(handle, "probe_number=" .. tostring(probes))
    append_line(handle, "star_system_body_count=" .. tostring(body_count))
    append_line(handle, "starmap_pawn_count=" .. tostring(pawn_count))
    append_line(handle, "starmap_actor_count=" .. tostring(actor_count))
    append_line(handle, "")

    append_line(handle, "[StarMapPawn_C]")
    for _, pawn in pairs(pawns) do
        append_line(handle, "full_name=" .. object_full_name(pawn))
        append_line(handle, "path_name=" .. object_path_name(pawn))
        append_line(handle, "PanBoundsHorizontal=" .. tostring(property_value(pawn, {"PanBoundsHorizontal", "pan_bounds_horizontal"})))
        append_line(handle, "PanBoundsVertical=" .. tostring(property_value(pawn, {"PanBoundsVertical", "pan_bounds_vertical"})))
        append_line(handle, "ZoomDistanceList=" .. tostring(property_value(pawn, {"ZoomDistanceList", "zoom_distance_list"})))
        append_line(handle, "ZoomLevelThresholds=" .. tostring(property_value(pawn, {"ZoomLevelThresholds", "zoom_level_thresholds"})))
    end
    append_line(handle, "")

    append_line(handle, "[StarMapActor_C]")
    for _, actor in pairs(actors) do
        append_line(handle, "full_name=" .. object_full_name(actor))
        append_line(handle, "path_name=" .. object_path_name(actor))
        append_line(handle, "star_system_body_lookup=" .. tostring(property_value(actor, {"StarSystemBodyLookUp", "star_system_body_look_up"})))
    end
    append_line(handle, "")

    append_line(handle, "[StarSystemBody_C Sample]")
    local sample_limit = 80
    local i = 0
    for _, body in pairs(bodies) do
        i = i + 1
        if i <= sample_limit then
            local id = property_value(body, {"StarSystemID", "StarSystemId", "star_system_id"})
            append_line(handle, string.format("%d|id=%s|%s", i, tostring(id), object_full_name(body)))
        end
    end

    handle:close()
    print(string.format("[TKURuntimeProbe] wrote %s probe; bodies=%d pawns=%d actors=%d\n", kind, body_count, pawn_count, actor_count))
end

print("[TKURuntimeProbe] loaded\n")

ExecuteWithDelay(10000, function()
    ExecuteInGameThread(function()
        dump_runtime_probe("delayed startup")
    end)
end)

LoopAsync(PROBE_INTERVAL_MS, function()
    ExecuteInGameThread(function()
        dump_runtime_probe("loop")
    end)
    if wrote_starmap_probe and probes >= 4 then
        return true
    end
    return probes >= MAX_PROBES
end)
