const std = @import("std");

test "detect leak" {
    var list = std.ArrayList(u21).init(std.testing.allocator);
    // mising 'defer list.deinit();'
    try list.append('y');
    try std.testing.expect(list.items.len == 1);
}
