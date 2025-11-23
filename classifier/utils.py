import plotly.graph_objs as go
import plotly.io as pio

def generate_confidence_chart(predictions):
    """
    Generates a Plotly bar chart HTML div from a prediction dictionary.
    """
    labels = list(predictions.keys())
    scores = list(predictions.values())
    
    # Clean up labels for display (e.g., "Apple___Apple_scab" -> "Apple Scab")
    clean_labels = [l.replace('Apple___', '').replace('_', ' ') for l in labels]

    # Create the Bar Chart
    bar = go.Bar(
        x=scores,
        y=clean_labels,
        orientation='h', # Horizontal bar
        marker=dict(color='#198754'), # Bootstrap success green color
        text=[f"{s:.1%}" for s in scores], # Show percentage on bar
        textposition='auto'
    )

    layout = go.Layout(
        title='<b>Confidence Analysis</b>',
        margin=dict(l=20, r=20, t=40, b=20),
        xaxis=dict(range=[0, 1], tickformat='.0%'), # Fix x-axis from 0% to 100%
        yaxis=dict(autorange="reversed"), # Top result at the top
        height=300,
        paper_bgcolor='rgba(0,0,0,0)', # Transparent background
        plot_bgcolor='rgba(0,0,0,0)'
    )

    fig = go.Figure(data=[bar], layout=layout)
    
    # Return just the HTML <div>, not the whole page
    return pio.to_html(fig, full_html=False, config={'displayModeBar': False})