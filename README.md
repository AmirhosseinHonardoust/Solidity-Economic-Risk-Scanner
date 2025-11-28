# **Solidity Economic Risk Scanner**

### **A Research-Grade Framework for Detecting Economic Vulnerabilities in Smart Contracts**

<p align="center">
  <img src="https://img.shields.io/badge/Solidity-0.8.x-black?style=for-the-badge&logo=solidity">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Security-Economic%20Analysis-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Research--Tool-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

# **Abstract**

Smart contract auditing today focuses primarily on traditional security issues: reentrancy, integer overflow, access control, and memory safety.
But the majority of real-world DeFi failures are **economic**, not technical:

* Protocols with unstable fee parameters
* Tokens engineered for slow-drain rugpulls
* Oracle manipulation points
* Unbounded inflation vectors
* Mispriced liquidations
* Weak collateralization logic
* Faulty AMM invariants
* Owner-controlled liquidity traps

**Solidity Economic Risk Scanner** introduces a new category of smart contract analysis:
**economic security analysis**, the examination of economic incentives, financial mechanisms, and system behavior encoded in smart contract logic.

This tool is designed to help researchers, auditors, builders, and investors identify economic fragility before it becomes an exploit, collapse, or systemic failure.

---

# **Why Economic Security Matter More Than Ever**

## **1. The largest DeFi losses weren’t from reentrancy, they were economic failures**

Examples:

| Vulnerability Type          | Example                    | Loss           |
| --------------------------- | -------------------------- | -------------- |
| **Oracle manipulation**     | Mango Markets              | $114M          |
| **Liquidity trap/honeypot** | Dozens of ERC-20 rugs      | massive        |
| **Toxic fee tokens**        | Hidden tax abuse tokens    | widespread     |
| **Bad LTV math**            | Multiple lending protocols | millions       |
| **Inflation minting**       | Admin mint exploits        | billions total |

Pure “code correctness” is not enough.

DeFi systems must be analyzed as **financial machines**, not just software.

---

# **What This Tool Actually Does**

The scanner performs **economic logic analysis**, not bytecode-level vulnerability enumeration.

It detects:

### **1. Control Risks (Authority & Admin Powers)**

* overuse of `onlyOwner`
* owner can mint tokens
* owner can arbitrarily change fees
* owner can blacklist users
* admin kill-switches
* upgradeable proxy exploitability

These are the same patterns found in real “slow rugs.”

---

### **2. Tokenomics Risks**

* unbounded minting
* deflationary tokens with excessive burns
* reflection/rebasing mechanics
* high tax on sells but low tax on buys
* fee structures that enable user lock-in
* inconsistent supply formulas

This is economic correctness analysis, not just code correctness.

---

### **3. Liquidity & Trading Risks**

* honeypots (cannot sell)
* blacklist/whitelist liquidity traps
* cooldown or anti-bot logic
* liquidity removal authority
* transfer gating based on owner logic

Many scam tokens abuse these patterns.

---

### **4. Oracle & Pricing Risks**

* owner-controlled oracle
* manual price setters
* lack of sanity checks
* no time-weighted pricing
* AMM-based pricing without slippage controls

These are critical for lending, AMMs, perp protocols.

---

### **5. Invariant & Parameter Risks**

Detects signals of missing:

* AMM invariants (`x * y = k`)
* safety bounds around LTV ratios
* collateral health-check logic
* liquidation buffers
* utilization caps

A DeFi system without bounds is economically unsafe.

---

# **Architecture (Deep Explanation)**

The project is structured as a **pipeline-based security engine**, similar to static analyzers but architected for **economic logic**.

```
            ┌────────────┐
            │  Loader    │
            └──────┬─────┘
                   │
            ┌──────▼─────┐
            │   Parser   │
            └──────┬─────┘
                   │
                   ▼
     ┌───────▶ Features ◀───────┐
     │             ┬             │
     │             │             │
     │      ┌──────▼─────┐       │
     │      │   Rules    │       │
     │      └──────┬─────┘       │
     │             │             │
     │      ┌──────▼─────┐       │
     └───── │   Scoring  │ ──────┘
            └──────┬─────┘
                   │
             ┌─────▼─────┐
             │ Reporting │
             └───────────┘
```

Each component is deliberately modular and extensible.

---

# **Module-by-Module Explanation**

## **1. Loader**

* Reads `.sol` files
* Recurses directories
* Builds `{filename → source_code}` mappings
* Handles CLI input

This part is stable and robust.

---

## **2. Parser (Currently Naive Placeholder)**

The parser currently creates a `ContractProfile` containing:

* contract name
* raw source code
* placeholders for functions/variables

This is designed to be replaced with:

* Tree-Sitter parser
* solc JSON AST
* solidity-parser Python port

Once AST is attached, feature extraction becomes extremely powerful.

---

## **3. Feature Extractors, The Core Intelligence Layer**

Each feature extractor analyzes **economic behavior signals**:

### `fees.py`, Fee & Tax Economics

Searches for:

* fee variables
* buy/sell tax structures
* transfer fee logic
* tax-based mint/burn manipulation

### `supply.py`, Token Supply Dynamics

Finds:

* mint / burn
* missing maxSupply
* elastic supply logic

### `roles.py`, Centralized Control

Detects:

* `onlyOwner`
* admin-only functions
* modifiers
* upgrade admin logic

### `liquidity.py`, Liquidity & Trading Patterns

Flags:

* blacklist
* whitelist
* cooldown
* antibot logic
* liquidity directionality

### `oracle.py`, Price Oracle Logic

Detects:

* Chainlink usage
* manual price setters
* custom AMM price code
* owner-controlled pricing

### `invariants.py`, Economic Invariant Patterns

Detects hints of:

* constant-product AMMs
* lending LTV ratios
* collateral health models

---

## **4. Rule Engine, Economic Vulnerability Checks**

Each rule looks at features and produces a `RiskFinding`.

Current rules include:

### ✔ `unbounded_mint_rule`

detects minting without cap → **HIGH RISK**

### ✔ `manual_price_rule`

detects `setPrice()` or `updatePrice()` → **HIGH RISK**

### ✔ `blacklist_mechanism_rule`

transfer lockout → **MEDIUM RISK**

### ✔ `centralized_control_rule`

excessive use of `onlyOwner` → **MEDIUM RISK**

### ✔ `fee_complexity_rule`

fee + tax → **MEDIUM RISK**

### ✔ `missing_safety_bounds_rule`

LTV or collateral mention without safety → **LOW RISK**

---

## **5. Risk Scoring Model**

Risk scoring uses weighted severities:

| Severity | Weight |
| -------- | ------ |
| LOW      | 1      |
| MEDIUM   | 3      |
| HIGH     | 7      |
| CRITICAL | 10     |

Scores map to levels:

| Score | Level    |
| ----- | -------- |
| 0     | NONE     |
| 1–4   | LOW      |
| 5–14  | MEDIUM   |
| 15–29 | HIGH     |
| 30+   | CRITICAL |

This makes scanning results comparable across many contracts.

---

## **6. Reporting**

### Text Output:

Readable summaries for CLI users:

```
[MEDIUM][CONTROL] Heavy reliance on onlyOwner modifiers
```

### JSON Output:

Machine-readable format for dashboards or ML pipelines.

---

# **Examples of Real Detection Outputs**

## Example 1, Honeypot Token

```
[MEDIUM][LIQUIDITY] Blacklist functionality detected
[MEDIUM][CONTROL] Heavy reliance on onlyOwner
```

## Example 2, Manual Oracle Token

```
[HIGH][ORACLE] Manual price setter detected
```

## Example 3, Unbounded Minting

```
[HIGH][SUPPLY] Mint function without explicit max supply
```

---

# **Example Contracts Provided**

The repository includes carefully curated contracts that emulate:

| File                            | Risk Class             |
| ------------------------------- | ---------------------- |
| owner_unbounded_mint.sol        | Inflation / Control    |
| variable_tax_token.sol          | Tokenomics / Fees      |
| honeypot_token.sol              | Liquidity trap         |
| blacklist_restrictions.sol      | Censorship / Liquidity |
| manual_oracle.sol               | Oracle manipulation    |
| unsafe_liquidation_lending.sol  | Lending risk           |
| broken_amm.sol                  | AMM invariant failure  |
| reflection_token.sol            | Complex tokenomics     |
| proxy_admin_kill_switch.sol     | Upgrade/Proxy risk     |
| whitelist_launch_token.sol      | Transfer gating        |
| burnable_infinite_inflation.sol | Burn + re-mint         |
| deflationary_tax_token.sol      | Deflation mechanics    |

These examples provide broad coverage of economic attack surfaces.

---

# **Deep Motivation & Research Context**

This project is based on the idea that:

> **Smart contracts are economic machines.**
> They encode incentives, permissions, and state transitions that define the behavior of a financial system.

Pure static security analysis can tell you if reentrancy is possible, but:

* It cannot tell you if the owner can rug liquidity.
* It cannot tell you if the fee logic traps users.
* It cannot tell you if minting breaks token value.
* It cannot tell you if LTV logic can create insolvency.
* It cannot tell you if price updates allow manipulation.

Economic failures require economic reasoning:

* What happens if the owner changes feeBps?
* Does minting dilute all holders?
* Does blacklist logic hide honeypot behavior?
* Does lending allow undercollateralization?
* Does AMM pricing deviate from expected invariants?

This tool analyzes **economic correctness**, not just **syntactic correctness**.

---

# **Future Extensions (Professional Roadmap)**

## **1. Full Solidity AST Integration**

Using:

* tree-sitter
* solc JSON AST
* solidity-parser

Enables precise detection of:

* control flow
* modifiers
* state variable types
* mappings
* mathematical expressions
* fee formulas
* event logging

---

## **2. ML-Based Rug Probability Model**

Train on a dataset of:

* known rugpulls
* known safe tokens
* known DeFi exploits

Features:

* fee patterns
* supply logic
* blacklist usage
* oracle patterns
* proxy patterns
* ownership concentration

Output:

* `rug_probability_score`

---

## **3. DeFi-Specific Modules**

* AMM invariant verification
* liquidation correctness
* interest rate model stability
* emission model simulation
* liquidity migration patterns

---

## **4. On-Chain Data Integration**

* Etherscan verified sources
* DEX liquidity states
* owner history
* token holder graphs
* real-time price feeds

Combining on-chain data + code analysis = powerful risk engine.

---

# **Disclaimers**

* This is a research tool.
* It does **not** replace a professional audit.
* Findings require human validation.
* Smart contract economics are complex and contextual.

Use responsibly and interpret results judiciously.
