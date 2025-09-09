from flask import Flask, render_template, jsonify, request, send_from_directory
from flask_cors import CORS
import os
import json

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
CORS(app)

# Datos de empresas Insurtech españolas embebidos
EMPRESAS_DATA = [
    {
        "id": 1,
        "nombre_oficial": "Tuio",
        "nombre_comercial": "Tuio Insurance",
        "descripcion_corta": "MGA digital que ofrece seguros de hogar, vida y mascotas mediante una plataforma digital",
        "propuesta_valor": "Simplificación del proceso de contratación y gestión de seguros a través de tecnología digital",
        "modelo_negocio": "MGA Digital",
        "tipo_relacion": "B2C",
        "ciudad": "Madrid",
        "pais": "España",
        "ano_fundacion": 2018,
        "empleados": 150,
        "financiacion_total": "€16.700.000",
        "sitio_web": "https://tuio.es",
        "email": "info@tuio.es",
        "linkedin": "https://linkedin.com/company/tuio",
        "categorias_insurtech": "MGA Digital, Seguros Digitales",
        "soluciones": [
            {
                "id": 1,
                "nombre": "Plataforma de Seguros Digitales",
                "descripcion": "Plataforma integral para contratación y gestión de seguros",
                "categoria_insurtech": "Digital Platform",
                "tecnologias": "React, Node.js, AI, Machine Learning"
            },
            {
                "id": 2,
                "nombre": "App Móvil",
                "descripcion": "Aplicación móvil para gestión completa de pólizas y siniestros",
                "categoria_insurtech": "Mobile App",
                "tecnologias": "React Native, iOS, Android"
            }
        ]
    },
    {
        "id": 2,
        "nombre_oficial": "Weecover",
        "nombre_comercial": "Weecover",
        "descripcion_corta": "Plataforma tecnológica de distribución de seguros (Insurance-as-a-Service) líder en seguros embebidos",
        "propuesta_valor": "Integración de seguros en plataformas de e-commerce mediante API",
        "modelo_negocio": "Insurance-as-a-Service",
        "tipo_relacion": "B2B",
        "ciudad": "Madrid",
        "pais": "España",
        "ano_fundacion": 2019,
        "empleados": 80,
        "financiacion_total": "€4.200.000",
        "sitio_web": "https://weecover.com",
        "email": "info@weecover.com",
        "linkedin": "https://linkedin.com/company/weecover",
        "categorias_insurtech": "Insurance-as-a-Service, Embedded Insurance",
        "soluciones": [
            {
                "id": 3,
                "nombre": "API de Seguros Embebidos",
                "descripcion": "API para integración de seguros en plataformas de e-commerce",
                "categoria_insurtech": "API Platform",
                "tecnologias": "REST API, Microservices, Cloud"
            },
            {
                "id": 4,
                "nombre": "Dashboard de Partners",
                "descripcion": "Panel de control para partners y gestión de pólizas embebidas",
                "categoria_insurtech": "Partner Platform",
                "tecnologias": "Vue.js, Python, Analytics"
            }
        ]
    },
    {
        "id": 3,
        "nombre_oficial": "Cobee",
        "nombre_comercial": "Cobee",
        "descripcion_corta": "Plataforma de beneficios sociales para empleados",
        "propuesta_valor": "Digitalización y gestión de beneficios sociales empresariales",
        "modelo_negocio": "Plataforma de Beneficios",
        "tipo_relacion": "B2B",
        "ciudad": "Barcelona",
        "pais": "España",
        "ano_fundacion": 2017,
        "empleados": 200,
        "financiacion_total": "€40.000.000",
        "sitio_web": "https://cobee.io",
        "email": "info@cobee.io",
        "linkedin": "https://linkedin.com/company/cobee",
        "categorias_insurtech": "HR Benefits, Employee Benefits",
        "soluciones": [
            {
                "id": 5,
                "nombre": "Plataforma de Beneficios Empresariales",
                "descripcion": "Plataforma integral para gestión de beneficios sociales empresariales",
                "categoria_insurtech": "HR Platform",
                "tecnologias": "Angular, Java, Microservices"
            }
        ]
    },
    {
        "id": 4,
        "nombre_oficial": "BDEO",
        "nombre_comercial": "BDEO",
        "descripcion_corta": "Tecnología de IA para gestión de siniestros y peritaje digital",
        "propuesta_valor": "Automatización del proceso de peritaje mediante inteligencia artificial",
        "modelo_negocio": "Tecnología de Siniestros",
        "tipo_relacion": "B2B",
        "ciudad": "Madrid",
        "pais": "España",
        "ano_fundacion": 2015,
        "empleados": 120,
        "financiacion_total": "€25.000.000",
        "sitio_web": "https://bdeo.io",
        "email": "info@bdeo.io",
        "linkedin": "https://linkedin.com/company/bdeo",
        "categorias_insurtech": "AI Claims, Computer Vision",
        "soluciones": [
            {
                "id": 6,
                "nombre": "Plataforma de IA para Siniestros",
                "descripcion": "Plataforma de IA para análisis automático de siniestros mediante imágenes",
                "categoria_insurtech": "AI Platform",
                "tecnologias": "Computer Vision, Deep Learning, Python"
            }
        ]
    },
    {
        "id": 5,
        "nombre_oficial": "Barkibu",
        "nombre_comercial": "Barkibu",
        "descripcion_corta": "Telemedicina veterinaria y seguros para mascotas",
        "propuesta_valor": "Consultas veterinarias online y seguros especializados para mascotas",
        "modelo_negocio": "Telemedicina Veterinaria",
        "tipo_relacion": "B2C",
        "ciudad": "Madrid",
        "pais": "España",
        "ano_fundacion": 2016,
        "empleados": 45,
        "financiacion_total": "€3.500.000",
        "sitio_web": "https://barkibu.com",
        "email": "info@barkibu.com",
        "linkedin": "https://linkedin.com/company/barkibu",
        "categorias_insurtech": "Pet Insurance, Telemedicine",
        "soluciones": [
            {
                "id": 7,
                "nombre": "Consulta Veterinaria Online",
                "descripcion": "Plataforma de telemedicina veterinaria con chat y videollamadas",
                "categoria_insurtech": "Telemedicine",
                "tecnologias": "WebRTC, React, Node.js"
            },
            {
                "id": 8,
                "nombre": "Seguros para Mascotas",
                "descripcion": "Seguros veterinarios especializados para mascotas",
                "categoria_insurtech": "Pet Insurance",
                "tecnologias": "Insurance Platform, Mobile App"
            }
        ]
    },
    {
        "id": 6,
        "nombre_oficial": "Insurama",
        "nombre_comercial": "Insurama",
        "descripcion_corta": "Seguros para dispositivos electrónicos y bienes de alto valor",
        "propuesta_valor": "Protección especializada para dispositivos tecnológicos",
        "modelo_negocio": "Seguros Tecnología",
        "tipo_relacion": "B2C",
        "ciudad": "Madrid",
        "pais": "España",
        "ano_fundacion": 2020,
        "empleados": 65,
        "financiacion_total": "€8.000.000",
        "sitio_web": "https://insurama.com",
        "email": "info@insurama.com",
        "linkedin": "https://linkedin.com/company/insurama",
        "categorias_insurtech": "Device Insurance, Technology Insurance",
        "soluciones": [
            {
                "id": 9,
                "nombre": "Seguros para Dispositivos",
                "descripcion": "Protección especializada para dispositivos tecnológicos",
                "categoria_insurtech": "Device Insurance",
                "tecnologias": "Digital Platform, IoT Integration"
            }
        ]
    },
    {
        "id": 7,
        "nombre_oficial": "Stoïk",
        "nombre_comercial": "Stoïk",
        "descripcion_corta": "Ciberseguros especializados para pymes",
        "propuesta_valor": "Protección cibernética especializada para pequeñas y medianas empresas",
        "modelo_negocio": "Ciberseguros",
        "tipo_relacion": "B2B",
        "ciudad": "Madrid",
        "pais": "España",
        "ano_fundacion": 2021,
        "empleados": 35,
        "financiacion_total": "€25.000.000",
        "sitio_web": "https://stoik.io",
        "email": "info@stoik.io",
        "linkedin": "https://linkedin.com/company/stoik",
        "categorias_insurtech": "Cyber Insurance, SME Insurance",
        "soluciones": [
            {
                "id": 10,
                "nombre": "Plataforma de Ciberseguros",
                "descripcion": "Protección cibernética especializada para pymes",
                "categoria_insurtech": "Cyber Insurance",
                "tecnologias": "Security Analytics, AI, Cloud"
            }
        ]
    },
    {
        "id": 8,
        "nombre_oficial": "Life5",
        "nombre_comercial": "Life5",
        "descripcion_corta": "Seguros de vida digitales con proceso simplificado",
        "propuesta_valor": "Seguros de vida con contratación 100% digital",
        "modelo_negocio": "Seguros de Vida Digital",
        "tipo_relacion": "B2C",
        "ciudad": "Barcelona",
        "pais": "España",
        "ano_fundacion": 2019,
        "empleados": 25,
        "financiacion_total": "€2.000.000",
        "sitio_web": "https://life5.es",
        "email": "info@life5.es",
        "linkedin": "https://linkedin.com/company/life5",
        "categorias_insurtech": "Life Insurance, Digital Insurance",
        "soluciones": [
            {
                "id": 11,
                "nombre": "Plataforma de Seguros de Vida",
                "descripcion": "Seguros de vida con contratación 100% digital",
                "categoria_insurtech": "Life Insurance",
                "tecnologias": "Digital Platform, AI Underwriting"
            }
        ]
    },
    {
        "id": 9,
        "nombre_oficial": "Swipet",
        "nombre_comercial": "Swipet",
        "descripcion_corta": "Seguros veterinarios y servicios para mascotas",
        "propuesta_valor": "Seguros veterinarios completos con red de clínicas",
        "modelo_negocio": "Seguros para Mascotas",
        "tipo_relacion": "B2C",
        "ciudad": "Valencia",
        "pais": "España",
        "ano_fundacion": 2018,
        "empleados": 40,
        "financiacion_total": "€3.000.000",
        "sitio_web": "https://swipet.com",
        "email": "info@swipet.com",
        "linkedin": "https://linkedin.com/company/swipet",
        "categorias_insurtech": "Pet Insurance, Veterinary Services",
        "soluciones": [
            {
                "id": 12,
                "nombre": "Seguros Veterinarios",
                "descripcion": "Seguros veterinarios completos con red de clínicas",
                "categoria_insurtech": "Pet Insurance",
                "tecnologias": "Veterinary Network, Mobile App"
            }
        ]
    },
    {
        "id": 10,
        "nombre_oficial": "Asistensi",
        "nombre_comercial": "Asistensi",
        "descripcion_corta": "Servicios de asistencia digital y seguros complementarios",
        "propuesta_valor": "Servicios de asistencia digital con tecnología avanzada",
        "modelo_negocio": "Asistencia Digital",
        "tipo_relacion": "B2C",
        "ciudad": "Sevilla",
        "pais": "España",
        "ano_fundacion": 2017,
        "empleados": 55,
        "financiacion_total": "€4.500.000",
        "sitio_web": "https://asistensi.com",
        "email": "info@asistensi.com",
        "linkedin": "https://linkedin.com/company/asistensi",
        "categorias_insurtech": "Digital Assistance, Emergency Services",
        "soluciones": [
            {
                "id": 13,
                "nombre": "Servicios de Asistencia 24/7",
                "descripcion": "Servicios de asistencia digital con tecnología avanzada",
                "categoria_insurtech": "Digital Assistance",
                "tecnologias": "AI Chatbots, Emergency Response"
            }
        ]
    }
]

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    static_folder_path = app.static_folder
    if static_folder_path is None:
        return "Static folder not configured", 404

    if path != "" and os.path.exists(os.path.join(static_folder_path, path)):
        return send_from_directory(static_folder_path, path)
    else:
        index_path = os.path.join(static_folder_path, 'index.html')
        if os.path.exists(index_path):
            return send_from_directory(static_folder_path, 'index.html')
        else:
            return "index.html not found", 404

@app.route('/api/companies')
def get_companies():
    return jsonify({
        'success': True,
        'companies': EMPRESAS_DATA
    })

@app.route('/api/companies/<int:company_id>')
def get_company(company_id):
    company = next((c for c in EMPRESAS_DATA if c['id'] == company_id), None)
    if company:
        return jsonify({
            'success': True,
            'company': company
        })
    return jsonify({
        'success': False,
        'error': 'Empresa no encontrada'
    }), 404

@app.route('/api/companies/<int:company_id>/solutions')
def get_company_solutions(company_id):
    company = next((c for c in EMPRESAS_DATA if c['id'] == company_id), None)
    if company:
        return jsonify({
            'success': True,
            'solutions': company.get('soluciones', [])
        })
    return jsonify({
        'success': False,
        'error': 'Empresa no encontrada'
    }), 404

@app.route('/api/companies/<int:company_id>/query', methods=['POST'])
def query_company_agent(company_id):
    data = request.get_json()
    question = data.get('question', '')
    
    company = next((c for c in EMPRESAS_DATA if c['id'] == company_id), None)
    if not company:
        return jsonify({
            'success': False,
            'error': 'Empresa no encontrada'
        }), 404
    
    # Generar respuesta simulada basada en los datos de la empresa
    response = f"""**Análisis de {company['nombre_oficial']}**

**Información Básica:**
- **Modelo de Negocio:** {company['modelo_negocio']}
- **Propuesta de Valor:** {company['propuesta_valor']}
- **Tipo de Relación:** {company['tipo_relacion']}

**Datos Corporativos:**
- **Fundación:** {company['ano_fundacion']}
- **Empleados:** {company['empleados']}
- **Financiación Total:** {company['financiacion_total']}
- **Ubicación:** {company['ciudad']}, {company['pais']}

**Contacto:**
- **Sitio Web:** {company['sitio_web']}
- **Email:** {company['email']}
- **LinkedIn:** {company['linkedin']}

**Soluciones y Tecnologías:**"""
    
    for solucion in company.get('soluciones', []):
        response += f"""
- **{solucion['nombre']}:** {solucion['descripcion']}
  - Categoría: {solucion['categoria_insurtech']}
  - Tecnologías: {solucion['tecnologias']}"""
    
    response += f"""

**Respuesta a tu pregunta:** "{question}"

Basándome en los datos de {company['nombre_oficial']}, esta empresa se especializa en {company['modelo_negocio'].lower()} y su principal diferenciador es {company['propuesta_valor'].lower()}. Con {company['empleados']} empleados y una financiación de {company['financiacion_total']}, se posiciona como una empresa sólida en el ecosistema Insurtech español."""
    
    return jsonify({
        'success': True,
        'response': response,
        'company': company['nombre_oficial']
    })

@app.route('/api/analysis/<analysis_type>', methods=['POST'])
def cross_analysis(analysis_type):
    if analysis_type == 'market':
        total_funding = sum(float(c['financiacion_total'].replace('€', '').replace('.', '').replace(',', '')) for c in EMPRESAS_DATA)
        total_employees = sum(c['empleados'] for c in EMPRESAS_DATA)
        
        response = f"""**Análisis Transversal del Mercado Insurtech Español**

**Métricas Generales:**
- **Total de empresas analizadas:** {len(EMPRESAS_DATA)}
- **Financiación total del ecosistema:** €{total_funding:,.0f}
- **Empleados totales:** {total_employees:,}
- **Financiación promedio por empresa:** €{total_funding/len(EMPRESAS_DATA):,.0f}

**Distribución por Modelo de Negocio:**"""
        
        models = {}
        for company in EMPRESAS_DATA:
            model = company['modelo_negocio']
            if model not in models:
                models[model] = []
            models[model].append(company['nombre_oficial'])
        
        for model, companies in models.items():
            response += f"\n- **{model}:** {len(companies)} empresas ({', '.join(companies)})"
        
        response += f"""

**Distribución Geográfica:**"""
        
        cities = {}
        for company in EMPRESAS_DATA:
            city = company['ciudad']
            if city not in cities:
                cities[city] = []
            cities[city].append(company['nombre_oficial'])
        
        for city, companies in cities.items():
            response += f"\n- **{city}:** {len(companies)} empresas ({', '.join(companies)})"
        
        response += f"""

**Distribución B2B vs B2C:**"""
        
        b2b = [c for c in EMPRESAS_DATA if c['tipo_relacion'] == 'B2B']
        b2c = [c for c in EMPRESAS_DATA if c['tipo_relacion'] == 'B2C']
        
        response += f"\n- **B2B:** {len(b2b)} empresas"
        response += f"\n- **B2C:** {len(b2c)} empresas"
        
        return jsonify({
            'success': True,
            'response': response,
            'analysis_type': 'Análisis de Mercado'
        })
    
    elif analysis_type == 'geographic':
        response = """**Análisis Geográfico del Ecosistema Insurtech Español**

**Distribución por Ciudades:**"""
        
        cities = {}
        for company in EMPRESAS_DATA:
            city = company['ciudad']
            if city not in cities:
                cities[city] = {'count': 0, 'companies': [], 'funding': 0, 'employees': 0}
            cities[city]['count'] += 1
            cities[city]['companies'].append(company['nombre_oficial'])
            cities[city]['funding'] += float(company['financiacion_total'].replace('€', '').replace('.', '').replace(',', ''))
            cities[city]['employees'] += company['empleados']
        
        for city, data in sorted(cities.items(), key=lambda x: x[1]['count'], reverse=True):
            response += f"""

**{city}:**
- **Empresas:** {data['count']} ({', '.join(data['companies'])})
- **Financiación total:** €{data['funding']:,.0f}
- **Empleados totales:** {data['employees']:,}
- **Financiación promedio:** €{data['funding']/data['count']:,.0f}"""
        
        response += f"""

**Concentración del Ecosistema:**
- **Madrid** domina el ecosistema con {cities.get('Madrid', {}).get('count', 0)} empresas
- **Barcelona** es el segundo hub con {cities.get('Barcelona', {}).get('count', 0)} empresas
- **Distribución geográfica** relativamente concentrada en grandes ciudades"""
        
        return jsonify({
            'success': True,
            'response': response,
            'analysis_type': 'Análisis Geográfico'
        })
    
    elif analysis_type == 'business':
        response = """**Análisis de Modelos de Negocio Insurtech**

**Distribución por Tipo de Modelo:**"""
        
        models = {}
        for company in EMPRESAS_DATA:
            model = company['modelo_negocio']
            if model not in models:
                models[model] = {'count': 0, 'companies': [], 'funding': 0, 'employees': 0}
            models[model]['count'] += 1
            models[model]['companies'].append(company['nombre_oficial'])
            models[model]['funding'] += float(company['financiacion_total'].replace('€', '').replace('.', '').replace(',', ''))
            models[model]['employees'] += company['empleados']
        
        for model, data in sorted(models.items(), key=lambda x: x[1]['count'], reverse=True):
            response += f"""

**{model}:**
- **Empresas:** {data['count']} ({', '.join(data['companies'])})
- **Financiación total:** €{data['funding']:,.0f}
- **Empleados totales:** {data['employees']:,}
- **Financiación promedio:** €{data['funding']/data['count']:,.0f}"""
        
        response += f"""

**Análisis de Relaciones B2B vs B2C:**"""
        
        b2b = [c for c in EMPRESAS_DATA if c['tipo_relacion'] == 'B2B']
        b2c = [c for c in EMPRESAS_DATA if c['tipo_relacion'] == 'B2C']
        
        b2b_funding = sum(float(c['financiacion_total'].replace('€', '').replace('.', '').replace(',', '')) for c in b2b)
        b2c_funding = sum(float(c['financiacion_total'].replace('€', '').replace('.', '').replace(',', '')) for c in b2c)
        
        response += f"""

**B2B ({len(b2b)} empresas):**
- Financiación total: €{b2b_funding:,.0f}
- Financiación promedio: €{b2b_funding/len(b2b):,.0f}
- Empresas: {', '.join([c['nombre_oficial'] for c in b2b])}

**B2C ({len(b2c)} empresas):**
- Financiación total: €{b2c_funding:,.0f}
- Financiación promedio: €{b2c_funding/len(b2c):,.0f}
- Empresas: {', '.join([c['nombre_oficial'] for c in b2c])}"""
        
        return jsonify({
            'success': True,
            'response': response,
            'analysis_type': 'Análisis de Modelos de Negocio'
        })
    
    return jsonify({
        'success': False,
        'error': 'Tipo de análisis no soportado'
    }), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
