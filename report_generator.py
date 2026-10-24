from jinja2 import Template

def generate_report(ip_data, protocol_data, suspicious_ips):
    template_html = """
    <html>
    <head><title>Network Traffic Report</title></head>
    <body>
        <h1>Traffic Analysis Report</h1>

        <h2>IP Activity</h2>
        <ul>
        {% for ip, count in ip_data.items() %}
            <li>{{ ip }} -> {{ count }} packets</li>
        {% endfor %}
        </ul>

        <h2>Protocols</h2>
        <ul>
        {% for proto, count in protocol_data.items() %}
            <li>{{ proto }} -> {{ count }}</li>
        {% endfor %}
         {% if 'OTHER' in protocol_data %}
            <li>OTHER -> {{ protocol_data['OTHER'] }}</li>
        {% endif %}

        </ul>

        <h2>Unusual IP Activity</h2>
        <ul>
        {% for ip, count in suspicious_ips %}
            
            {% if count > 50 %}
                {% set reason = "Possible DDoS activity" %}
            {% elif count > 30 %}
                {% set reason = "High traffic, possible scanning" %}
            {% else %}
                {% set reason = "Normal but slightly unusual traffic" %}
            {% endif %}

            <li>
                {{ ip }} -> {{ count }} packets ({{ reason }})
            </li>

        {% endfor %}
        </ul>
    </body>
    </html>
    """

    template = Template(template_html)
    html_content = template.render(
        ip_data=ip_data,
        protocol_data=protocol_data,
        suspicious_ips=suspicious_ips
    )

    with open("report.html", "w") as f:
        f.write(html_content)

    print("[+] Report generated -> report.html")
