class Package:
    base_r = "כלי עגול 250 גרם"
    base_b = "כלי פלסטיק 0.5 ליטר"
    u = "יחידה"

    double_r = "כלי עגול 500 גרם"
    double_b = "כלי פלסטיק 1 ליטר"

    def is_base(self, p):
        return p in [self.base_b, self.base_r, self.u]

    def is_dabel(self, p):
        return p in [self.double_b, self.double_r]

    def package_factor(self, p: str) -> int:
        # cookies type save as Package
        # return 1 if self.is_base(p) else 2
        return 2 if self.is_dabel(p) else 1
