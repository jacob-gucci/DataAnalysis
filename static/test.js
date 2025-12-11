// thanks to https://www.chartjs.org/docs/latest/getting-started/usage.html

new Chart(
document.getElementById('container'),
{
  type: 'bar',
  data: {
    labels: data.map(agent => agent.agent_name),
    datasets: [
      {
        label: 'Average Active Days by Agent',
        data: data.map(agent => agent.active_days)
      },
      {
        label: 'Average Hold Days by Agent',
        data: data.map(agent => agent.hold_days)
      }
    ]
  }
}
);