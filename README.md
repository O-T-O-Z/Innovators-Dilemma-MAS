# Innovator's Dilemma Multi-Agent System

## Market

- each cell: set of customers
    - customers take highest 
        - $\text{decision\_factor} = \alpha\cdot \text{company.proximity} + \beta\cdot \text{company.performance}$
- companies have a location (a cell: [x, y])
- companies earn `companies.ncustomers * product.profit`

## CompanyAgent
- randomly spawned on Market (grid) (two agents can't be on same cell)
### Attributes:
- capital
- product (new class)
    - profit per customer per step
    - performance (different max S curve)
- distance (proximity) to customers

- innovation_cost = strategy.innovation_factor * resources_spent_per_step
    - R&D => new candidates
    - Adopt foreigner candidates (later addition)
- exploitation_cost = (1-strategy.innovation_factor) * resources_spent_per_step

### Actions

**explore -> R&D | Aquisition**
```
capital := capital - innovation_cost
```
**exploit -> Improve**
```
company.product.improve()
copmany.capital := copmany.capital - exploitation_cost
```

# Further considerations
- form alliance -> ? (later addition)
- acquisition -> ? (later addition)
- patents

