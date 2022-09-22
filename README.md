# Innovator's Dilemma Multi-Agent System

## Market (Grid)

- each cell: a customer (agent)
    - customers choose company $o_j$ with highest decision factor $df$:
        - Decision concerning customer $c_i$ for company $j$
    $$
    df_{ij} = \alpha\cdot o_j.proximity + \gamma \cdot naive\_factor + \\ min(\beta\cdot o_j.performance, c_i.satisfaction)
    $$
    - Customer will choose a company with the highest 
    - init to a random company at first (spawn after company agents)
    - `proximity`: if $\alpha$ is low, then it means that proximity does not matter as much (e.g., online products).
    - `naive_factor`: a random number that influences the decision and potentially models irrational decisions due to psychological factors or beliefs about companies. The main assumption about this constant is that decisions are not always rational, so better companies who have better products are not always be guaranteed to be chosen (e.g., unsustainable, unethical, product was not perceived correctly).  
    - `satisfaction`: is the value of the decision factor where a higher performance does not matter. For example, customers generally do not need more than 1GB/s internet speed and so they do not need to switch if another company sells wifi with higher speed.

## Company (Agent)
### Attributes:
- initial location (cell: [x, y] randomly spawned on grid two agents can't be on same cell)
- capital = random(100, 10000)
- customer_base: a set of customers grid points allocated to the company
- company $o_j$ 
$$
o_j.profit_t =  o_j.profit\_margin \cdot ||o_j.customers||
$$
- product [new class]
    - performance (different max S curve)
    - random improvement rate 
- A candidate product emerges for company $o_j$:
$$
    P(candidate)_t = r\cdot P(candidate)_{t-1} \cdot o_j.innovation\_factor \cdot o_j.rd\_quality \\
    o_j.rd\_quality = c \cdot o_j.capital \\
$$
- Once a candidate product emerges, the innovation resources are spent into improving the product, and after $o_j.patience$ number of steps, the company will give up and search for new candidate products. Otherwise, the company will replace its product with its new candidate product.

$$
o_j.capital_t = o_j.capital_{t-1} + o_j.profit_t - o_j.innovation\_cost_t - o_j.exploitation\_cost_t \\
o_j.innovation\_cost = o_j.budget_t * o_j.innovation\_factor \\
o_j.exploitation\_cost = o_j.budget_t * (1-o_j.innovation\_factor)
$$

* **Acquisition**: a company can buy another company and obtain its technology. The company also buys its risks and its challenges. The only difference is that the two companies will now share the capital. Acquisition will reduce the buyer's capital.

acquire(a, b) => b loses its identity and a and b will have the identity of a. a loses an amount of capital (b.value).

$$
o_j.value_t = r_{value} \cdot o_j.value_{t-1} + \alpha\cdot ||o_j.customers|| + \beta\cdot o_j.product.performance_t
$$


* **Alliance**: allies(a, b) => a and b share customers

# Further considerations
- patents
- Adopt foreigner candidates (later addition)
