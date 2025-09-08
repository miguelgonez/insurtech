#!/usr/bin/env python3
"""
Sistema Insurtech con datos embebidos para deployment
"""

import os
import sys
import json
from datetime import datetime

# DON'T CHANGE THIS !!!
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory, jsonify, request
from flask_cors import CORS

app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

# Configurar CORS para permitir todas las solicitudes
CORS(app)

# Datos embebidos de empresas Insurtech españolas
EMPRESAS_DATA = [
    {
        "id": 1,
        "nombre_oficial": "Tuio",
        "nombre_comercial": "Tuio Insurance",
        "descripcion_corta": "MGA digital que ofrece seguros de hogar, vida y mascotas mediante una plataforma digital",
        "propuesta_valor": "Simplificación del proceso de contratación y gestión de seguros a través de tecnología digital",
        "modelo_negocio": "MGA Digital",
        "tipo_relacion": "B2C",
        "sitio_web": "https://tuio.es",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2018,
        "numero_empleados": 150,
        "financiacion_total": 16700000,
        "email": "info@tuio.es",
        "linkedin": "https://linkedin.com/company/tuio",
        "categorias_insurtech": "Digital Insurance, MGA"
    },
    {
        "id": 2,
        "nombre_oficial": "Weecover",
        "nombre_comercial": "Weecover",
        "descripcion_corta": "Plataforma tecnológica de distribución de seguros líder en seguros embebidos",
        "propuesta_valor": "Insurance-as-a-Service para e-commerce y plataformas digitales",
        "modelo_negocio": "Insurance-as-a-Service",
        "tipo_relacion": "B2B",
        "sitio_web": "https://weecover.com",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2017,
        "numero_empleados": 80,
        "financiacion_total": 4200000,
        "email": "contact@weecover.com",
        "linkedin": "https://linkedin.com/company/weecover",
        "categorias_insurtech": "Embedded Insurance, B2B Platform"
    },
    {
        "id": 3,
        "nombre_oficial": "Cobee",
        "nombre_comercial": "Cobee",
        "descripcion_corta": "Plataforma de gestión de beneficios sociales para empleados",
        "propuesta_valor": "Digitalización y optimización de beneficios sociales empresariales",
        "modelo_negocio": "Plataforma de Beneficios",
        "tipo_relacion": "B2B",
        "sitio_web": "https://cobee.io",
        "ciudad": "Barcelona",
        "pais": "España",
        "año_fundacion": 2017,
        "numero_empleados": 200,
        "financiacion_total": 40000000,
        "email": "hello@cobee.io",
        "linkedin": "https://linkedin.com/company/cobee",
        "categorias_insurtech": "HR Benefits, Employee Insurance"
    },
    {
        "id": 4,
        "nombre_oficial": "BDEO",
        "nombre_comercial": "BDEO",
        "descripcion_corta": "Tecnología de IA para gestión de siniestros y peritaje digital",
        "propuesta_valor": "Automatización de procesos de siniestros mediante visión artificial e IA",
        "modelo_negocio": "Tecnología de Siniestros",
        "tipo_relacion": "B2B",
        "sitio_web": "https://bdeo.io",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2017,
        "numero_empleados": 120,
        "financiacion_total": 25000000,
        "email": "info@bdeo.io",
        "linkedin": "https://linkedin.com/company/bdeo",
        "categorias_insurtech": "AI Claims, Computer Vision"
    },
    {
        "id": 5,
        "nombre_oficial": "Barkibu",
        "nombre_comercial": "Barkibu",
        "descripcion_corta": "Telemedicina veterinaria y seguros para mascotas",
        "propuesta_valor": "Consultas veterinarias online y seguros especializados para mascotas",
        "modelo_negocio": "Telemedicina Veterinaria",
        "tipo_relacion": "B2C",
        "sitio_web": "https://barkibu.com",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2016,
        "numero_empleados": 45,
        "financiacion_total": 3500000,
        "email": "info@barkibu.com",
        "linkedin": "https://linkedin.com/company/barkibu",
        "categorias_insurtech": "Pet Insurance, Telemedicine"
    },
    {
        "id": 6,
        "nombre_oficial": "Fintonic",
        "nombre_comercial": "Fintonic",
        "descripcion_corta": "Plataforma de gestión financiera personal con productos de seguros",
        "propuesta_valor": "Gestión financiera integral con recomendaciones personalizadas de seguros",
        "modelo_negocio": "Fintech/Insurtech",
        "tipo_relacion": "B2C",
        "sitio_web": "https://fintonic.com",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2012,
        "numero_empleados": 180,
        "financiacion_total": 32000000,
        "email": "info@fintonic.com",
        "linkedin": "https://linkedin.com/company/fintonic",
        "categorias_insurtech": "Personal Finance, Insurance Marketplace"
    },
    {
        "id": 7,
        "nombre_oficial": "Insurama",
        "nombre_comercial": "Insurama",
        "descripcion_corta": "Seguros para dispositivos electrónicos y bienes de alto valor",
        "propuesta_valor": "Protección especializada para dispositivos tecnológicos con proceso digital",
        "modelo_negocio": "Seguros Tecnología",
        "tipo_relacion": "B2C",
        "sitio_web": "https://insurama.com",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2015,
        "numero_empleados": 65,
        "financiacion_total": 8000000,
        "email": "info@insurama.com",
        "linkedin": "https://linkedin.com/company/insurama",
        "categorias_insurtech": "Device Insurance, Technology Protection"
    },
    {
        "id": 8,
        "nombre_oficial": "Stoïk",
        "nombre_comercial": "Stoïk",
        "descripcion_corta": "Ciberseguros especializados para pymes",
        "propuesta_valor": "Protección cibernética accesible y especializada para pequeñas y medianas empresas",
        "modelo_negocio": "Ciberseguros",
        "tipo_relacion": "B2B",
        "sitio_web": "https://stoik.io",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2020,
        "numero_empleados": 35,
        "financiacion_total": 25000000,
        "email": "contact@stoik.io",
        "linkedin": "https://linkedin.com/company/stoik",
        "categorias_insurtech": "Cyber Insurance, SME Protection"
    },
    {
        "id": 9,
        "nombre_oficial": "Life5",
        "nombre_comercial": "Life5",
        "descripcion_corta": "Seguros de vida digitales con proceso simplificado",
        "propuesta_valor": "Seguros de vida accesibles con contratación 100% digital",
        "modelo_negocio": "Seguros de Vida Digital",
        "tipo_relacion": "B2C",
        "sitio_web": "https://life5.es",
        "ciudad": "Barcelona",
        "pais": "España",
        "año_fundacion": 2019,
        "numero_empleados": 25,
        "financiacion_total": 2000000,
        "email": "info@life5.es",
        "linkedin": "https://linkedin.com/company/life5",
        "categorias_insurtech": "Life Insurance, Digital Process"
    },
    {
        "id": 10,
        "nombre_oficial": "Swipet",
        "nombre_comercial": "Swipet",
        "descripcion_corta": "Seguros veterinarios y servicios para mascotas",
        "propuesta_valor": "Seguros veterinarios completos con red de clínicas asociadas",
        "modelo_negocio": "Seguros para Mascotas",
        "tipo_relacion": "B2C",
        "sitio_web": "https://swipet.com",
        "ciudad": "Valencia",
        "pais": "España",
        "año_fundacion": 2018,
        "numero_empleados": 40,
        "financiacion_total": 3000000,
        "email": "info@swipet.com",
        "linkedin": "https://linkedin.com/company/swipet",
        "categorias_insurtech": "Pet Insurance, Veterinary Network"
    },
    {
        "id": 11,
        "nombre_oficial": "Vitaance",
        "nombre_comercial": "Vitaance",
        "descripcion_corta": "Seguros de salud digitales con enfoque preventivo",
        "propuesta_valor": "Seguros de salud con servicios de prevención y bienestar digital",
        "modelo_negocio": "Seguros de Salud Digital",
        "tipo_relacion": "B2C",
        "sitio_web": "https://vitaance.com",
        "ciudad": "Madrid",
        "pais": "España",
        "año_fundacion": 2020,
        "numero_empleados": 30,
        "financiacion_total": 1500000,
        "email": "info@vitaance.com",
        "linkedin": "https://linkedin.com/company/vitaance",
        "categorias_insurtech": "Health Insurance, Preventive Care"
    },
    {
        "id": 12,
        "nombre_oficial": "Asistensi",
        "nombre_comercial": "Asistensi",
        "descripcion_corta": "Servicios de asistencia digital y seguros complementarios",
        "propuesta_valor": "Servicios de asistencia 24/7 con tecnología digital avanzada",
        "modelo_negocio": "Asistencia Digital",
        "tipo_relacion": "B2C",
        "sitio_web": "https://asistensi.com",
        "ciudad": "Sevilla",
        "pais": "España",
        "año_fundacion": 2017,
        "numero_empleados": 55,
        "financiacion_total": 4500000,
        "email": "info@asistensi.com",
        "linkedin": "https://linkedin.com/company/asistensi",
        "categorias_insurtech": "Digital Assistance, Emergency Services"
    }
]

# Datos de soluciones por empresa
SOLUCIONES_DATA = [
    {
        "id": 1,
        "empresa_id": 1,
        "nombre": "Plataforma de Seguros Digitales",
        "descripcion": "Plataforma integral para contratación y gestión de seguros de hogar, vida y mascotas",
        "categoria_insurtech": "Digital Platform",
        "tecnologias": "React, Node.js, AI, Machine Learning"
    },
    {
        "id": 2,
        "empresa_id": 1,
        "nombre": "App Móvil Tuio",
        "descripcion": "Aplicación móvil para gestión completa de pólizas y siniestros",
        "categoria_insurtech": "Mobile App",
        "tecnologias": "React Native, iOS, Android"
    },
    {
        "id": 3,
        "empresa_id": 2,
        "nombre": "API de Seguros Embebidos",
        "descripcion": "API para integración de seguros en plataformas de e-commerce",
        "categoria_insurtech": "API Platform",
        "tecnologias": "REST API, Microservices, Cloud"
    },
    {
        "id": 4,
        "empresa_id": 2,
        "nombre": "Dashboard de Partners",
        "descripcion": "Panel de control para partners y gestión de pólizas embebidas",
        "categoria_insurtech": "Partner Platform",
        "tecnologias": "Vue.js, Python, Analytics"
    },
    {
        "id": 5,
        "empresa_id": 3,
        "nombre": "Plataforma de Beneficios",
        "descripcion": "Plataforma integral para gestión de beneficios sociales empresariales",
        "categoria_insurtech": "HR Platform",
        "tecnologias": "Angular, Java, Microservices"
    },
    {
        "id": 6,
        "empresa_id": 4,
        "nombre": "BDEO Vision",
        "descripcion": "Plataforma de IA para análisis automático de siniestros mediante imágenes",
        "categoria_insurtech": "AI Platform",
        "tecnologias": "Computer Vision, Deep Learning, Python"
    },
    {
        "id": 7,
        "empresa_id": 5,
        "nombre": "Consulta Veterinaria Online",
        "descripcion": "Plataforma de telemedicina veterinaria con chat y videollamadas",
        "categoria_insurtech": "Telemedicine",
        "tecnologias": "WebRTC, React, Node.js"
    },
    {
        "id": 8,
        "empresa_id": 6,
        "nombre": "Gestor Financiero Personal",
        "descripcion": "App de gestión financiera con recomendaciones de seguros personalizadas",
        "categoria_insurtech": "Personal Finance",
        "tecnologias": "Machine Learning, Open Banking, React Native"
    }
]

@app.route('/api/agents/companies', methods=['GET'])
def list_companies():
    """Listar todas las empresas disponibles"""
    try:
        return jsonify({
            'success': True,
            'companies': EMPRESAS_DATA,
            'total': len(EMPRESAS_DATA)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/agents/companies/<company_identifier>/query', methods=['POST'])
def query_company(company_identifier):
    """Consultar empresa específica"""
    try:
        data = request.get_json()
        if not data or 'question' not in data:
            return jsonify({
                'success': False,
                'error': 'Se requiere el campo "question" en el cuerpo de la petición'
            }), 400
        
        question = data['question']
        
        # Buscar empresa
        company = None
        try:
            company_id = int(company_identifier)
            company = next((c for c in EMPRESAS_DATA if c['id'] == company_id), None)
        except ValueError:
            company = next((c for c in EMPRESAS_DATA if company_identifier.lower() in c['nombre_oficial'].lower()), None)
        
        if not company:
            return jsonify({
                'success': False,
                'error': 'Empresa no encontrada'
            }), 404
        
        # Buscar soluciones de la empresa
        solutions = [s for s in SOLUCIONES_DATA if s['empresa_id'] == company['id']]
        
        # Generar respuesta basada en los datos
        response = f"""Información detallada sobre {company['nombre_oficial']}:

📋 DATOS BÁSICOS:
- Nombre oficial: {company['nombre_oficial']}
- Nombre comercial: {company.get('nombre_comercial', 'N/A')}
- Descripción: {company.get('descripcion_corta', 'N/A')}
- Propuesta de valor: {company.get('propuesta_valor', 'N/A')}

💼 MODELO DE NEGOCIO:
- Tipo: {company['modelo_negocio']}
- Relación: {company['tipo_relacion']}
- Categorías: {company.get('categorias_insurtech', 'N/A')}

🏢 INFORMACIÓN CORPORATIVA:
- Fundación: {company.get('año_fundacion', 'N/A')}
- Empleados: {company.get('numero_empleados', 'N/A')}
- Ubicación: {company.get('ciudad', 'N/A')}, {company.get('pais', 'N/A')}
- Financiación total: €{company.get('financiacion_total', 0):,} EUR

🌐 CONTACTO:
- Web: {company.get('sitio_web', 'N/A')}
- Email: {company.get('email', 'N/A')}
- LinkedIn: {company.get('linkedin', 'N/A')}

🔧 SOLUCIONES ({len(solutions)}):"""
        
        for solution in solutions:
            response += f"""
- {solution['nombre']}: {solution['descripcion']}
  Tecnologías: {solution.get('tecnologias', 'N/A')}"""
        
        response += f"""

❓ PREGUNTA: {question}

💡 ANÁLISIS: Basándome en los datos disponibles, {company['nombre_oficial']} es una empresa {company['modelo_negocio']} con enfoque {company['tipo_relacion']} que se especializa en {company.get('categorias_insurtech', 'servicios insurtech')}. 

La empresa fue fundada en {company.get('año_fundacion', 'fecha no especificada')} y cuenta con {company.get('numero_empleados', 'un número no especificado de')} empleados. Su propuesta de valor se centra en {company.get('propuesta_valor', 'la innovación en el sector asegurador')}.

Con una financiación total de €{company.get('financiacion_total', 0):,}, la empresa ha desarrollado {len(solutions)} soluciones principales que abordan diferentes aspectos del mercado asegurador."""
        
        return jsonify({
            'success': True,
            'empresa': company['nombre_oficial'],
            'pregunta': question,
            'respuesta': response
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/agents/companies/<int:company_id>/solutions', methods=['GET'])
def get_company_solutions(company_id):
    """Obtener soluciones de una empresa específica"""
    try:
        company = next((c for c in EMPRESAS_DATA if c['id'] == company_id), None)
        if not company:
            return jsonify({
                'success': False,
                'error': 'Empresa no encontrada'
            }), 404
        
        solutions = [s for s in SOLUCIONES_DATA if s['empresa_id'] == company_id]
        
        return jsonify({
            'success': True,
            'company': company['nombre_oficial'],
            'solutions': solutions,
            'total': len(solutions)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/agents/analysis/types', methods=['GET'])
def list_analysis_types():
    """Listar tipos de análisis disponibles"""
    types = {
        'market_segments': 'Segmentación del mercado Insurtech español',
        'business_models': 'Análisis de modelos de negocio',
        'funding_analysis': 'Análisis de financiación y inversión',
        'technology_trends': 'Tendencias tecnológicas del sector',
        'competitive_landscape': 'Panorama competitivo',
        'geographic_distribution': 'Distribución geográfica',
        'demo_analysis': 'Análisis de demostración'
    }
    
    return jsonify({
        'success': True,
        'analysis_types': types
    })

@app.route('/api/agents/analysis/<analysis_type>', methods=['POST'])
def perform_analysis(analysis_type):
    """Realizar análisis del ecosistema"""
    try:
        if analysis_type == 'market_segments':
            # Análisis de segmentación
            b2b_count = len([c for c in EMPRESAS_DATA if c['tipo_relacion'] == 'B2B'])
            b2c_count = len([c for c in EMPRESAS_DATA if c['tipo_relacion'] == 'B2C'])
            
            result = f"""📊 SEGMENTACIÓN DEL MERCADO INSURTECH ESPAÑOL

🏢 TOTAL DE EMPRESAS ANALIZADAS: {len(EMPRESAS_DATA)}

🎯 DISTRIBUCIÓN POR TIPO DE RELACIÓN:
- B2B (Business to Business): {b2b_count} empresas ({b2b_count/len(EMPRESAS_DATA)*100:.1f}%)
- B2C (Business to Consumer): {b2c_count} empresas ({b2c_count/len(EMPRESAS_DATA)*100:.1f}%)

📈 MODELOS DE NEGOCIO IDENTIFICADOS:"""
            
            models = {}
            for company in EMPRESAS_DATA:
                model = company['modelo_negocio']
                models[model] = models.get(model, 0) + 1
            
            for model, count in models.items():
                percentage = (count / len(EMPRESAS_DATA)) * 100
                result += f"\n- {model}: {count} empresas ({percentage:.1f}%)"
        
        elif analysis_type == 'funding_analysis':
            # Análisis de financiación
            total_funding = sum(c.get('financiacion_total', 0) for c in EMPRESAS_DATA)
            funded_companies = len([c for c in EMPRESAS_DATA if c.get('financiacion_total', 0) > 0])
            avg_funding = total_funding / funded_companies if funded_companies > 0 else 0
            
            result = f"""💰 ANÁLISIS DE FINANCIACIÓN INSURTECH ESPAÑOL

💼 RESUMEN FINANCIERO:
- Financiación total del ecosistema: €{total_funding:,} EUR
- Empresas con financiación: {funded_companies} de {len(EMPRESAS_DATA)} ({funded_companies/len(EMPRESAS_DATA)*100:.1f}%)
- Financiación promedio: €{avg_funding:,.0f} EUR

🏆 TOP 5 EMPRESAS POR FINANCIACIÓN:"""
            
            sorted_companies = sorted(EMPRESAS_DATA, key=lambda x: x.get('financiacion_total', 0), reverse=True)[:5]
            for i, company in enumerate(sorted_companies, 1):
                funding = company.get('financiacion_total', 0)
                result += f"\n{i}. {company['nombre_oficial']}: €{funding:,} EUR"
        
        elif analysis_type == 'geographic_distribution':
            # Análisis geográfico
            cities = {}
            for company in EMPRESAS_DATA:
                city = company.get('ciudad', 'No especificada')
                cities[city] = cities.get(city, 0) + 1
            
            result = f"""🗺️ DISTRIBUCIÓN GEOGRÁFICA INSURTECH ESPAÑOL

📍 CONCENTRACIÓN POR CIUDADES:"""
            
            for city, count in sorted(cities.items(), key=lambda x: x[1], reverse=True):
                percentage = (count / len(EMPRESAS_DATA)) * 100
                result += f"\n- {city}: {count} empresas ({percentage:.1f}%)"
        
        else:
            result = f"""📋 ANÁLISIS: {analysis_type.replace('_', ' ').title()}

Este análisis se basa en {len(EMPRESAS_DATA)} empresas Insurtech españolas identificadas en nuestra base de datos.

El ecosistema Insurtech español muestra una gran diversidad en modelos de negocio y enfoques tecnológicos, con empresas que van desde MGAs digitales hasta plataformas de seguros embebidos y soluciones de IA para siniestros.

Características destacadas:
- Diversificación en modelos B2B y B2C
- Concentración geográfica en Madrid y Barcelona
- Fuerte inversión en tecnologías emergentes
- Enfoque en digitalización de procesos tradicionales"""
        
        return jsonify({
            'success': True,
            'result': result
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/agents/demo', methods=['GET'])
def demo():
    """Ejecutar demo del sistema"""
    try:
        demo_results = [
            {
                'type': 'company_query',
                'company': 'Tuio',
                'question': '¿Cuál es la propuesta de valor de esta empresa?',
                'result': {
                    'success': True,
                    'respuesta': 'Tuio es una MGA digital que simplifica el proceso de contratación y gestión de seguros de hogar, vida y mascotas a través de una plataforma completamente digital. Su propuesta de valor se centra en la digitalización completa del customer journey asegurador.'
                }
            },
            {
                'type': 'cross_analysis',
                'analysis': 'market_segments',
                'result': {
                    'success': True,
                    'result': f'El mercado Insurtech español cuenta con {len(EMPRESAS_DATA)} empresas principales, mostrando diversificación en modelos B2B y B2C, con predominio de soluciones digitales y creciente adopción de IA.'
                }
            }
        ]
        
        return jsonify({
            'success': True,
            'demo_results': demo_results
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/agents/health', methods=['GET'])
def health_check():
    """Verificar estado del sistema"""
    try:
        return jsonify({
            'success': True,
            'status': 'healthy',
            'companies_available': len(EMPRESAS_DATA),
            'solutions_available': len(SOLUCIONES_DATA),
            'version': 'embedded_data',
            'data_source': 'embedded'
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'status': 'unhealthy',
            'error': str(e)
        }), 500

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)

