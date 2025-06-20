operation GenerateRandomBit() : Result {
    use q = Qubit();
    H(q);
    return M(q);  // "Zufälliges" Ergebnis (0 oder 1)
}