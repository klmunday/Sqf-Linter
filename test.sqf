/*
    test file for SQF Linter
*/

private _a = "a";
private _b = 3;

hint _a;
systemChat (3 * (2 + _b));

if ((0xA == 10) && {10 == $A}) then {
    hint "equal";
} else {
    hint "not equal";
};

hint (1 <= 3);
MyGlobalTest = "test";
MyGlobalTest
