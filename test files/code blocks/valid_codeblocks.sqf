private _testCode = {
    hint "test";
    systemChat str 1 + 2;
};

[] call _testCode;
[] spawn _testCode;