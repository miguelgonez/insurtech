# Sistema de Agentes Insurtech España - Proyecto Completo

## Resumen Ejecutivo

Se ha desarrollado un sistema completo de análisis de empresas Insurtech españolas utilizando agentes de IA especializados. El proyecto incluye una base de datos exhaustiva, agentes especializados por empresa, agentes transversales para análisis de mercado, y una interfaz moderna desarrollada en React con TypeScript.

## Arquitectura del Sistema

### 1. Base de Datos SQLite
- **Archivo**: `insurtech_espana.db`
- **Estructura**: Relaciones 1:1 y 1:n entre empresas y soluciones
- **Campos**: Compatibles con estructura Crunchbase
- **Contenido**: 12 empresas Insurtech españolas con información detallada

### 2. Backend API Flask
- **Framework**: Flask con Python 3.11
- **Ubicación**: `/home/ubuntu/insurtech_agents_api/`
- **Puerto**: 5000
- **Características**:
  - API RESTful completa
  - Integración con LangChain y LangGraph
  - CORS habilitado
  - Manejo de errores robusto

### 3. Sistema de Agentes IA

#### Agentes Especializados por Empresa (LangChain)
- **Archivo**: `simple_company_agents.py`
- **Funcionalidad**: Un agente especializado por cada empresa
- **Capacidades**: Responde preguntas específicas sobre cada empresa
- **Modelo**: OpenAI GPT-4

#### Agentes Transversales (LangGraph)
- **Archivo**: `cross_analysis_agents.py`
- **Funcionalidad**: Análisis comparativo y de mercado
- **Tipos de análisis**:
  - Segmentación de mercado
  - Análisis de financiación
  - Tendencias tecnológicas
  - Análisis competitivo
  - Reportes comprehensivos

### 4. Frontend React TypeScript
- **Framework**: React 19 + TypeScript
- **Ubicación**: `/home/ubuntu/insurtech-frontend/`
- **Puerto**: 5173
- **Tecnologías**:
  - Vite para desarrollo
  - Tailwind CSS para estilos
  - shadcn/ui para componentes
  - Lucide React para iconos

## Empresas Incluidas en la Base de Datos

| Empresa | Modelo de Negocio | Tipo | Propuesta de Valor |
|---------|-------------------|------|-------------------|
| **Tuio** | MGA Digital | B2C | Seguros de hogar, vida y mascotas digitales |
| **Weecover** | Insurance-as-a-Service | B2B | Seguros embebidos para e-commerce |
| **Cobee** | Plataforma de Beneficios | B2B | Gestión de beneficios sociales |
| **BDEO** | Tecnología de Siniestros | B2B | IA para gestión de siniestros |
| **Barkibu** | Telemedicina Veterinaria | B2C | Consultas veterinarias online |
| **Fintonic** | Fintech/Insurtech | B2C | Gestión financiera personal |
| **Insurama** | Seguros Tecnología | B2C | Seguros para dispositivos electrónicos |
| **Stoïk** | Ciberseguros | B2B | Seguros cibernéticos para pymes |
| **Life5** | Seguros de Vida | B2C | Seguros de vida digitales |
| **Swipet** | Seguros para Mascotas | B2C | Seguros veterinarios |
| **Vitaance** | Seguros de Salud | B2C | Seguros de salud digitales |
| **Asistensi** | Asistencia Digital | B2C | Servicios de asistencia |

## Ecosistema Complementario

### Aceleradoras e Iniciativas
- **Mundi Lab Insurtech Accelerator** (Madrid) - Principal aceleradora
- **AEFI** - Asociación Española de Fintech & Insurtech
- **Insurtech Community Hub (ICH)** - Plataforma de networking

## Funcionalidades Implementadas

### 1. Consultas por Empresa
- Selección visual de empresas
- Formulario de consultas personalizadas
- Respuestas detalladas de agentes especializados
- Historial de consultas

### 2. Análisis Transversal
- Múltiples tipos de análisis disponibles
- Consultas personalizadas opcionales
- Análisis comparativo del ecosistema
- Reportes detallados

### 3. Sistema de Demostración
- Consultas de ejemplo automatizadas
- Demostración de capacidades del sistema
- Casos de uso reales

## APIs Disponibles

### Endpoints de Empresas
- `GET /api/agents/companies` - Lista todas las empresas
- `POST /api/agents/companies/{id}/query` - Consulta a agente especializado

### Endpoints de Análisis
- `GET /api/agents/analysis/types` - Tipos de análisis disponibles
- `POST /api/agents/analysis/{type}` - Ejecuta análisis transversal

### Endpoints de Sistema
- `GET /api/agents/health` - Estado del sistema
- `GET /api/agents/demo` - Ejecuta demostración completa

## Instalación y Despliegue

### Backend Flask
```bash
cd insurtech_agents_api
source venv/bin/activate
pip install -r requirements.txt
python src/main.py
```

### Frontend React
```bash
cd insurtech-frontend
pnpm install
pnpm run dev --host
```

## URLs de Acceso

- **Frontend React**: https://5173-ivtyg5qii33qpymqrnojo-4f3fc520.manusvm.computer
- **API Backend**: https://5000-ivtyg5qii33qpymqrnojo-4f3fc520.manusvm.computer

## Estructura de Archivos

```
/home/ubuntu/
├── insurtech_agents_api/           # Backend Flask
│   ├── src/
│   │   ├── main.py                # Aplicación principal
│   │   ├── routes/agents.py       # Rutas de la API
│   │   ├── simple_company_agents.py  # Agentes por empresa
│   │   ├── cross_analysis_agents.py  # Agentes transversales
│   │   └── static/index.html      # Frontend HTML original
│   ├── insurtech_espana.db        # Base de datos SQLite
│   ├── venv/                      # Entorno virtual Python
│   └── requirements.txt           # Dependencias Python
│
├── insurtech-frontend/             # Frontend React TypeScript
│   ├── src/
│   │   ├── App.tsx               # Componente principal
│   │   ├── main.tsx              # Punto de entrada
│   │   └── components/ui/        # Componentes UI
│   ├── public/                   # Archivos públicos
│   ├── package.json              # Dependencias Node.js
│   └── tsconfig.json             # Configuración TypeScript
│
└── Documentación/
    ├── empresas_insurtech_inicial.md
    ├── esquema_crunchbase_analisis.md
    └── empresas_soluciones_estructurado.md
```

## Tecnologías Utilizadas

### Backend
- **Python 3.11** - Lenguaje de programación
- **Flask** - Framework web
- **SQLite** - Base de datos
- **LangChain** - Framework para agentes IA
- **LangGraph** - Orquestación de agentes
- **OpenAI GPT-4** - Modelo de lenguaje

### Frontend
- **React 19** - Biblioteca de UI
- **TypeScript** - Tipado estático
- **Vite** - Herramienta de desarrollo
- **Tailwind CSS** - Framework CSS
- **shadcn/ui** - Componentes UI
- **pnpm** - Gestor de paquetes

## Características Técnicas

### Seguridad
- Variables de entorno para API keys
- CORS configurado correctamente
- Validación de entrada en APIs

### Performance
- Agentes inicializados al arranque
- Conexiones de base de datos optimizadas
- Frontend con lazy loading

### Escalabilidad
- Arquitectura modular
- APIs RESTful estándar
- Base de datos relacional normalizada

## Casos de Uso

### 1. Análisis de Empresa Específica
**Ejemplo**: "¿Cuál es la propuesta de valor de Tuio y cómo se diferencia de sus competidores?"
**Resultado**: Análisis detallado de la empresa con contexto del mercado

### 2. Análisis de Mercado
**Ejemplo**: Segmentación del mercado Insurtech español
**Resultado**: Categorización de empresas por modelo de negocio y target

### 3. Análisis de Inversión
**Ejemplo**: Tendencias de financiación en el sector
**Resultado**: Análisis de rondas de inversión y valoraciones

## Próximos Desarrollos

### Funcionalidades Pendientes
- [ ] Sistema de autenticación y autorización
- [ ] Persistencia de sesiones y consultas
- [ ] Exportación de reportes en PDF
- [ ] Integración con APIs externas (Crunchbase, etc.)
- [ ] Notificaciones en tiempo real
- [ ] Análisis predictivo con ML

### Mejoras Técnicas
- [ ] Tests unitarios y de integración
- [ ] Documentación API con Swagger
- [ ] Containerización con Docker
- [ ] CI/CD pipeline
- [ ] Monitoreo y logging avanzado
- [ ] Cache distribuido con Redis

## Conclusiones

El sistema desarrollado proporciona una plataforma completa para el análisis del ecosistema Insurtech español, combinando:

1. **Base de datos exhaustiva** con información verificada de empresas
2. **Agentes IA especializados** para análisis detallado
3. **Interfaz moderna** desarrollada con tecnologías actuales
4. **Arquitectura escalable** preparada para crecimiento futuro

El proyecto demuestra la viabilidad de utilizar agentes de IA especializados para el análisis sectorial, proporcionando insights valiosos tanto a nivel de empresa individual como de ecosistema completo.

