# 🏢 Sistema de Agentes Insurtech España

Sistema completo de análisis inteligente del ecosistema Insurtech español con agentes especializados de IA.

## 🚀 Demo en Vivo

**URL:** [https://0vhlizcgnxyn.manus.space](https://0vhlizcgnxyn.manus.space)

## ✨ Características Principales

### 📊 Base de Datos Completa
- **10 empresas Insurtech españolas** con datos reales
- **Campos tipo Crunchbase**: financiación, empleados, contacto, ubicación
- **24 soluciones catalogadas** con tecnologías y categorías
- **Relaciones 1:1 y 1:n** entre empresas y soluciones

### 🔍 Sistema de Filtros Avanzados
- **Búsqueda por texto libre** en tiempo real
- **Filtro por empresa específica** (dropdown)
- **Filtro por ubicación** (Madrid, Barcelona, Valencia, Sevilla)
- **Filtro por propuesta de valor** (MGA Digital, Insurance-as-a-Service, etc.)
- **Contador dinámico** de empresas filtradas
- **Botón limpiar filtros** cuando hay filtros activos

### 🤖 Agentes Especializados
- **Agente por empresa** con conocimiento específico
- **Consultas en lenguaje natural** sobre cada empresa
- **Respuestas detalladas** basadas en datos reales
- **Análisis de propuestas de valor** y diferenciación

### 📈 Análisis Transversal
- **Análisis de Mercado**: métricas generales, financiación total, distribución
- **Análisis Geográfico**: concentración por ciudades con datos detallados
- **Análisis de Modelos de Negocio**: comparativa B2B vs B2C

### 🎨 Interfaz Tipo Streamlit
- **Menú lateral** con empresas y filtros
- **Navegación por pestañas** (Consultas, Análisis, Demo)
- **Diseño responsive** para móvil y desktop
- **Actualización automática** al cambiar empresa

## 🏢 Empresas Incluidas

1. **Tuio** - MGA Digital (Madrid) - €16.7M
2. **Weecover** - Insurance-as-a-Service (Madrid) - €4.2M
3. **Cobee** - Plataforma de Beneficios (Barcelona) - €40M
4. **BDEO** - Tecnología de Siniestros (Madrid) - €25M
5. **Barkibu** - Telemedicina Veterinaria (Madrid) - €3.5M
6. **Insurama** - Seguros Tecnología (Madrid) - €8M
7. **Stoïk** - Ciberseguros (Madrid) - €25M
8. **Life5** - Seguros de Vida Digital (Barcelona) - €2M
9. **Swipet** - Seguros para Mascotas (Valencia) - €3M
10. **Asistensi** - Asistencia Digital (Sevilla) - €4.5M

**Total del ecosistema:** €131.9M en financiación, 815 empleados

## 🛠️ Tecnologías Utilizadas

### Backend
- **Flask** - Framework web Python
- **SQLite** - Base de datos embebida
- **LangChain** - Framework para agentes IA
- **OpenAI API** - Modelos de lenguaje

### Frontend
- **HTML5/CSS3** - Interfaz moderna
- **JavaScript Vanilla** - Funcionalidad sin dependencias
- **Responsive Design** - Compatible móvil y desktop

### Deployment
- **Manus Cloud** - Plataforma de deployment
- **Git** - Control de versiones

## 🚀 Instalación y Uso

### Requisitos Previos
```bash
Python 3.8+
pip (gestor de paquetes Python)
```

### Instalación
```bash
# Clonar repositorio
git clone https://github.com/miguelgonez/insurtech.git
cd insurtech

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
python src/main.py
```

### Acceso
```
http://localhost:5002
```

## 📱 Uso del Sistema

### 1. Explorar Empresas
- Usa el menú lateral para navegar entre empresas
- Aplica filtros para encontrar empresas específicas
- Haz clic en una empresa para ver información detallada

### 2. Consultar Agentes
- Selecciona una empresa
- Ve a la pestaña "Consultas por Empresa"
- Escribe tu pregunta en el campo de texto
- Haz clic en "Consultar Agente"

### 3. Análisis Transversal
- Ve a la pestaña "Análisis Transversal"
- Selecciona el tipo de análisis deseado
- Obtén insights del ecosistema completo

### 4. Demo del Sistema
- Ve a la pestaña "Demo"
- Ejecuta el demo completo para ver todas las funcionalidades

## 🔧 Estructura del Proyecto

```
insurtech/
├── src/
│   ├── main.py              # Aplicación Flask principal
│   └── static/
│       └── index.html       # Interfaz frontend
├── requirements.txt         # Dependencias Python
└── README.md               # Documentación
```

## 📊 API Endpoints

### Empresas
- `GET /api/companies` - Lista todas las empresas
- `GET /api/companies/<id>` - Detalles de empresa específica
- `POST /api/companies/<id>/query` - Consulta al agente especializado

### Análisis
- `POST /api/analysis/market` - Análisis de mercado
- `POST /api/analysis/geographic` - Análisis geográfico
- `POST /api/analysis/business` - Análisis de modelos de negocio

## 🎯 Casos de Uso

### Para Inversores
- Analizar el ecosistema Insurtech español
- Identificar oportunidades de inversión
- Comparar empresas por métricas clave

### Para Emprendedores
- Estudiar la competencia
- Identificar nichos de mercado
- Analizar modelos de negocio exitosos

### Para Investigadores
- Obtener datos del sector Insurtech
- Realizar análisis comparativos
- Generar insights del mercado

## 🔄 Actualizaciones Recientes

### v2.0 (Enero 2025)
- ✅ Interfaz tipo Streamlit completamente funcional
- ✅ Filtros desplegables avanzados
- ✅ Análisis transversal completo
- ✅ Consultas a agentes IA operativas
- ✅ Diseño responsive para móvil
- ✅ 10 empresas con datos actualizados

## 📞 Contacto

**Desarrollado por:** Miguel González  
**GitHub:** [miguelgonez](https://github.com/miguelgonez)  
**Proyecto:** [insurtech](https://github.com/miguelgonez/insurtech)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

**🎉 Sistema completamente funcional y listo para usar**

