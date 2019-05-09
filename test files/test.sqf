private _yesmyfren = { _i < 10; _b > 5 };
hint _test;
private '_test1';
for [{private _i = 0 }, {True}, { _i = _i + 1 }] do {
    systemChat str _i;
    private _test1 = "test";
    private _test = 5;
    hint _test;
};
hint _test1;
systemChat _test;
