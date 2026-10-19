## 1. Start the delivery metrics service

From the Lab 6 directory, activate your virtual environment if you use one, then run:

```bash
source .venv/bin/activate
python3 delivery_metrics.py
```

The terminal should report that the HTTP server has started on port `8000` and that delivery simulation is running. Keep this terminal open while monitoring the metrics.

If your virtual environment has a different name, activate that environment instead.

## 2. Check Prometheus

Open:

```text
http://localhost:9090
```

To view configured alerts, open:

```text
http://localhost:9090/alerts
```

The screenshots show the `delivery_alerts` rule group and these alert rules:

- **HighPendingDeliveries** — expression: `pending_deliveries > 10`, with a 15-second pending duration and warning severity.
- **HighAverageDeliveryTime** — also configured in the `delivery_alerts` group.

## 3. View the Grafana dashboard

Open Grafana at the address configured for your setup. 

- `total_deliveries`
- `pending_deliveries`
- `on_the_way_deliveries`
- Average Delivery Time

## 4. Run the Jenkins pipeline

Open:

```text
http://localhost:8080
```

Select **Delivery-Pipeline** and run **Build Now** (or the equivalent build action in your Jenkins UI). Open the build number and select **Console Output** to inspect the pipeline logs.
