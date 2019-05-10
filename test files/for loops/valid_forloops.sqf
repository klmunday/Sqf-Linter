// Should put the value of _i into the chat box 5 times
for [{private _i = 0}, {_i < 5}, {_i = _i + 1}] do {
	systemChat str _i;
};

// Does the same with other syntax
for "_i" from 0 to 4 do {systemChat str _i};

// Does the same but with different values
for "_i" from 0 to 9 step 2 do {systemChat str _i};
