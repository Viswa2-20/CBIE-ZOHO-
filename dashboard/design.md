# Analytics Dashboard Design 📊

## Overview
The CBIE Dashboard provides real-time insights into bot performance, user intent, and revenue impact.

## Key Metrics

### 1. Intent Distribution (Pie Chart)
- **Visual**: Donut chart showing the breakdown of user intents.
- **Segments**: Ready to Buy (Green), Researching (Blue), Support (Orange), Pricing (Purple).
- **Insight**: Helps identify if traffic is high-intent or mostly support-related.

### 2. Sentiment Heatmap (Time Series)
- **Visual**: Line chart with color gradient (Red=Negative, Green=Positive).
- **X-Axis**: Time (Hourly/Daily).
- **Y-Axis**: Average Sentiment Score (-1 to +1).
- **Insight**: Tracks customer satisfaction trends over time.

### 3. Recommendation Performance (Bar Chart)
- **Visual**: Horizontal bar chart of Top Recommended Products vs. Click-Through Rate (CTR).
- **Metric**: Conversion Rate % for each product recommendation.

### 4. Bot Impact (Scorecards)
- **Revenue Generated**: Total value of "Ready to Buy" users who converted.
- **Support Deflection**: % of "Support Needed" queries resolved without human agent.
- **Avg. Response Time**: ML inference latency.

## Implementation (Mockup)
The dashboard can be built using **Streamlit** or **React + Recharts**, connecting to the MongoDB `behavior_logs` and `intent_logs` collections.

```python
# Streamlit Example
import streamlit as st
import pandas as pd

st.title("CBIE Analytics Command Center")

col1, col2 = st.columns(2)
col1.metric("Active Sessions", "1,234", "+12%")
col2.metric("Avg Sentiment", "0.85", "+0.05")

st.subheader("Intent Breakdown")
# ... Plotly chart code ...
```
