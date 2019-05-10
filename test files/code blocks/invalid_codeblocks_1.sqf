private _testCode = {
    hint "test"
    systemChat str 1 + 2
};

[] call compile str _testCode;
[] spawn _testCode;