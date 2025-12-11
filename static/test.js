// thanks to https://d3js.org/getting-started

import * as d3 from "https://cdn.jsdelivr.net/npm/d3@7/+esm";

const width = 1856;
const height = 500;
const marginTop = 30;
const marginRight = 0;
const marginBottom = 30;
const marginLeft = 40;

const x = d3.scaleBand(d3.groupSort(data, ([d]) => -d.avg_hold_days, (d) => d.agent), [0, 100])
        .range([marginLeft, width - marginRight])
      .padding(0.1);

console.log(d3.max(data, (d) => d.avg_hold_days));
const y = d3.scaleLinear().domain([0, d3.max(data, (d) => d.avg_hold_days)])
        .range([height - marginBottom, marginTop]);

// Create the SVG container.
const svg = d3.create("svg")
    .attr("width", width)
    .attr("height", height);

// Add the x-axis.
svg.append("g")
    .attr("transform", `translate(0,${height - marginBottom})`)
    .call(d3.axisBottom(x));

// Add the y-axis.
svg.append("g")
    .attr("transform", `translate(${marginLeft},0)`)
    .call(d3.axisLeft(y));

svg.append("g")
      .attr("fill", "steelblue")
    .selectAll()
    .data(data)
    .join("rect")
      .attr("x", (d) => x(d.agent))
      .attr("y", (d) => y(d.avg_hold_days))
      .attr("height", (d) => y(0) - y(d.avg_hold_days))
      .attr("width", x.bandwidth());

// Append the SVG element.
container.append(svg.node());