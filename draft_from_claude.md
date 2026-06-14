# ByteBites — UML Class Diagram

```
┌─────────────────────────────────┐          ┌─────────────────────────────────────┐
│            Customer             │          │              FoodItem               │
├─────────────────────────────────┤          ├─────────────────────────────────────┤
│ - name: str                     │          │ - name: str                         │
│ - purchase_history: List[Order] │          │ - price: float                      │
├─────────────────────────────────┤          │ - category: str                     │
│ + add_purchase(order: Order)    │          │ - popularity_rating: float          │
│ + is_real_user(): bool          │          ├─────────────────────────────────────┤
└─────────────────────────────────┘          │ + get_details(): str                │
          │                                   └─────────────────────────────────────┘
          │ places                                   ▲                    ▲
          │ 0..*                                     │ contains           │ selects
          ▼                                          │ 0..*               │ 1..*
┌─────────────────────────────────┐          ┌───────┴─────────────────────────────┐
│             Order               │          │                Menu                 │
├─────────────────────────────────┤          ├─────────────────────────────────────┤
│ - items: List[FoodItem]         │◇────────▶│ - items: List[FoodItem]             │
│ - total_cost: float             │ selected ├─────────────────────────────────────┤
├─────────────────────────────────┤          │ + add_item(item: FoodItem)          │
│ + add_item(item: FoodItem)      │          │ + filter_by_category(cat): List[..] │
│ + compute_total(): float        │          └─────────────────────────────────────┘
└─────────────────────────────────┘
```

## Relationships

| From | To | Type | Multiplicity | Meaning |
|------|-----|------|--------------|---------|
| Customer → Order | aggregation | 1 → 0..* | A customer holds a `purchase_history` of past orders |
| Menu ◇→ FoodItem | aggregation | 1 → 0..* | The menu holds the full collection of food items |
| Order ◇→ FoodItem | aggregation | 1 → 1..* | An order references the selected food items |

## Notes on the mapping to the spec

- **Customer** — `name` and `purchase_history` (line 3); `is_real_user()` supports "verify they are real users."
- **FoodItem** — `name`, `price`, `category`, `popularity_rating` (line 5).
- **Menu** — holds all items and `filter_by_category("Drinks" | "Desserts")` (line 7).
- **Order** — groups selected items into a single transaction and computes `total_cost` (line 9).
