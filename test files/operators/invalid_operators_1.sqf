private _results = 2 * (5 % 2 + 12) // 4 - 1^2;
private _true = !False;
private _false = not True;
private _or = True || False or True;
private _and = True and False && True;
private _xor = ((True || False) && !!(False && True));
private _nor = !(True | True);
private _nand = !(False & False);
private _eq = 1 = 1;
private _neq = 1 != 2;
private _lt = 1 << 2;
private _lte = 1 <= 2;
private _gt = 2 > 1;
private _gte = 2 >= 1;
private _arr = [1, 2] + [3, 4]; // equals [1, 2, 3, 4]
private _string = "hello " + "world";
