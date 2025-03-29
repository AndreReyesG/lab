//! A destructing assigment can separate elements of indexable aggregate types (Tuples, Arrays, Vectors)
const print = @import("std").debug.print;

pub fn main() void {
    var x: i32 = undefined;
    var y: i32 = undefined;
    var z: i32 = undefined;

    const tuple = .{ 1, 2, 3 };
    x, y, z = tuple;
    print("tuple: x = {}, y = {}, z = {}\n", .{ x, y, z });

    const array = [_]u32{ 4, 5, 6 };
    x, y, z = array;
    print("array: x = {}, y = {}, z = {}\n", .{ x, y, z });

    const vector: @Vector(3, u32) = .{ 7, 8, 9 };
    x, y, z = vector;
    print("vector: x = {}, y = {}, z = {}\n", .{ x, y, z });
}
