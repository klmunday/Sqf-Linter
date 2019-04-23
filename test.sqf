private _i = "test";
for [{private _a = 0}, {_a != 1}, {_a = _a + 0.1}] do {
    systemChat str _i;
};