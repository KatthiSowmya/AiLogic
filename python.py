def consolidate_ranges(ranges):
    if not ranges:
        return []
    ranges.sort(key=lambda x: x[0])
    consolidated = [ranges[0]]
    for current in ranges[1:]:
        last = consolidated[-1]
        if current[0] <= last[1] + 1:
            consolidated[-1] = (last[0], max(last[1], current[1]))
        else:
            consolidated.append(current)
    return consolidated