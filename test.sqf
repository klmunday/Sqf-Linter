/*
    test file for SQF Linter
*/

private _a = "a";
private _b = 3;

hint _a;
systemChat (3 * (2 + _b));

if ((0xA == 10) && (10 == $A)) then {
    private _if = 'if block entered';
    hint _if;
} else {
    private _else = "else block entered";
    hint _else;
};

hint (1 <= 3);
MyGlobalTest = "test";

if (1 isEqualTo 1) then {
    private _scoped = "scoped variable";
    hint _scoped;
    /*  doesn't work for some reason (nested codeblocks)
    if (1 == 1) then {
        private _nested = "nested var";
    };
    */
} else {
    hint _scoped;  // shouldn't work

    private _scoped_else = "else";
    hint _scoped_else;
};

private _test = "test";
hint _scoped;  // shouldn't work
