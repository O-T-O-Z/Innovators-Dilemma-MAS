# Innovator's Dilemma Multi-Agent System

## Market (Grid)

- each cell: a customer
    - customers choose company with highest decision factor $df$:
        - Decision concerning customer $i$ for company $j$
    $$
    df_{ij} = \alpha\cdot company_j.proximity + \gamma \cdot naive\_factor() + \\ min(\beta\cdot company_j.performance, customer_i.satisfaction)
    $$
    - Customer will choose a company with the highest 
    - init to a random company at first
    - `proximity`: if $\alpha$ is low, then it means that proximity does not matter as much (e.g., online products).
    - `naive_factor`: a random number that influences the decision and potentially models irrational decisions due to psychological factors or beliefs about companies. The main assumption about this constant is that decisions are not always rational, so better companies who have better products are not always be gauranteed to be chosen (e.g., unsustainable, unethical).  
    - `satisfaction`: is the value of the decision factor where a higher performance does not matter. For example, customers generally do not need more than 1GB/s internet speed and so they do not need to switch if another company sells wifi with higher speed.

## Company (Agent)
- randomly spawned on Market (grid) (two agents can't be on same cell)
### Attributes:
- initial location (cell: [x, y])
- capital = random(100, 10000)
- customer_base: a set of customers grid points allocated to the company
- companies earn `companies.ncustomers * product.profit`
- product [new class]
    - profit per customer per step
    - performance (different max S curve)
    - random improvement rate 

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

