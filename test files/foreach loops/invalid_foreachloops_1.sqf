// Outputs 5 messages of a range 1-5
{
	private _val = _x + 1;
    systemChat str _val
} forEach 1;  // this SHOULD fail!

{
	private _val = _x + 1;
    systemChat str _val
} forEach "test"; // this SHOULD fail!
