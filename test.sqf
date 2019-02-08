hint _b;
if (true) then {
    private _b = "_b value";
    if (true) then {
        hint _b;
        private _b = "test";
        if (true) then {};
    },
    _b = "new value";
};
private _B = 2 + 2 + 2,
hint _b;
_b = 1,
_b
