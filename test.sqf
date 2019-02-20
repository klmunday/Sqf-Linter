hint _b;
private _test = if (true);
if (true) then {
    private _b = "_b value";
    if (true) then {
        hint _b;
        private _b = "_b if value";
        if (true) then {};
    },
    _b = "new value";
};
private _B = 2 + 2 + 2,
hint _b;
_b = 1,
if (true) then {
    hint "true";
} else {
    hint "false";
};
_b
