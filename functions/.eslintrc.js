module.exports = {
  root: true,
  extends: [
    "airbnb-base",
    "plugin:@typescript-eslint/recommended",
    "plugin:@typescript-eslint/recommended-requiring-type-checking",
    "prettier",
  ],
  parser: "@typescript-eslint/parser",
  parserOptions: {
    project: "./tsconfig.json",
  },
  settings: {
    "import/resolver": { typescript: {} },
  },
  rules: {
    "import/extensions": ["error", "ignorePackages", { ts: "never" }],
    "import/order": [
      "error",
      {
        groups: ["builtin", "external", ["internal", "parent", "sibling", "index"], "type"],
        pathGroups: [
          {
            pattern: "xxx/**",
            group: "internal",
            position: "before",
          },
        ],
        distinctGroup: false,
        pathGroupsExcludedImportTypes: ["builtin"],
        "newlines-between": "always",
        alphabetize: { order: "asc", caseInsensitive: true },
      },
    ],
    "import/prefer-default-export": "off",
  },
  ignorePatterns: [".eslintrc.js"],
};
