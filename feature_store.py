from feast import Entity, Field, FeatureView, FileSource, ValueType

# Define Entity
customer = Entity(name="customer_id", value_type=ValueType.INT64)

# Define CSV Source
customer_source = FileSource(path="customer_data.csv")

# Define Feature View
customer_features = FeatureView(
    name="customer_features",
    entities=[customer],
    schema=[
        Field(name="tenure", dtype=ValueType.INT64),
        Field(name="MonthlyCharges", dtype=ValueType.DOUBLE),
        Field(name="TotalCharges", dtype=ValueType.DOUBLE),
        Field(name="Churn", dtype=ValueType.BOOL),
    ],
    source=customer_source,
)
