# ByteBites — UML Class Diagram (Revised)

```
┌──────────────────────────────────────┐        ┌──────────────────────────────────────┐
│               Customer               │        │               FoodItem               │
│  «a person using the app»            │        │  «one product you can buy»           │
├──────────────────────────────────────┤        ├──────────────────────────────────────┤
│ - name: str                          │        │ - name: str                          │
│ - purchase_history: List[Order]      │        │ - price: float                       │
│     (their past orders)              │        │ - category: str  (e.g. "Drinks")     │
├──────────────────────────────────────┤        │ - popularity_rating: float           │
│ + add_purchase(order: Order)         │        │     (how well-liked it is)           │
│ + is_real_user(): bool               │        ├──────────────────────────────────────┤
│     (verify they're a real customer) │        │ + get_details(): str                 │
└──────────────────────────────────────┘        └──────────────────────────────────────┘
            │                                            ▲                      ▲
            │ places                                     │ contains             │ selects
            │ 0..*  (zero or more orders)                │ 0..* (all items)     │ 1..* (one or more)
            ▼                                            │                      │
┌──────────────────────────────────────┐        ┌───────┴──────────────────────────────┐
│                Order                 │        │                 Menu                 │
│  «one checkout / transaction»        │        │  «the full list of food we sell»     │
├──────────────────────────────────────┤        ├──────────────────────────────────────┤
│ - items: List[FoodItem]              │◇──────▶ │ - items: List[FoodItem]              │
│     (the items chosen)               │selected│     (every item offered)             │
│ - total_cost: float                  │        ├──────────────────────────────────────┤
│     (added up automatically)         │        │ + add_item(item: FoodItem)           │
├──────────────────────────────────────┤        │ + filter_by_category(cat): List[..]  │
│ + add_item(item: FoodItem)           │        │     (show just "Drinks", "Desserts") │
│ + compute_total(): float             │        └──────────────────────────────────────┘
└──────────────────────────────────────┘
```

## Relationships

| From | To | Type | Multiplicity | In plain words |
|------|-----|------|--------------|----------------|
| Customer → Order | aggregation | 1 → 0..* | A customer *places* orders and keeps them as purchase history |
| Menu ◇→ FoodItem | aggregation | 1 → 0..* | The menu *is a collection of* all food items |
| Order ◇→ FoodItem | aggregation | 1 → 1..* | An order *is made up of* the selected food items |

## Notes on the mapping to the spec

- **Customer** — `name` and `purchase_history`; `is_real_user()` supports "verify they are real users."
- **FoodItem** — `name`, `price`, `category`, `popularity_rating` 
- **Menu** — holds all items and `filter_by_category("Drinks" | "Desserts")`
- **Order** — groups selected items into a single transaction and computes `total_cost`
