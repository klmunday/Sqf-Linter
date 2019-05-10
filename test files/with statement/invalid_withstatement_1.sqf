uiNamespace setVariable ["test", 5];
with "uiNamespace" do {
	hint format ["value: %1", test];
};
