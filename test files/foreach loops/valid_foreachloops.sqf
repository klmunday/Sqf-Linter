// Outputs 5 messages of a range 1-5
{
	private _val = _x + 1;
    systemChat str _val
} forEach [0, 1, 2, 3, 4];

{
	private _val = _x + 1;
    systemChat str _val
} forEach position player;
