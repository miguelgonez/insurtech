# 🚀 Sistema de Agentes Insurtech España

Sistema completo de análisis de empresas Insurtech españolas con agentes especializados de IA, interfaz tipo Streamlit y base de datos exhaustiva.

## 🌐 Demo en Vivo

**[Ver Demo Funcionando](https://e5h6i7cvpdd8.manus.space)**

*Nota: Si tienes problemas de acceso por restricciones de red, ejecuta el proyecto localmente siguiendo las instrucciones de instalación.*

## 📋 Descripción

Este proyecto proporciona un análisis completo del ecosistema Insurtech español mediante:

- **Base de datos exhaustiva** con 10 empresas Insurtech españolas
- **Interfaz tipo Streamlit** desarrollada en React + TypeScript
- **Sistema de agentes especializados** con LangChain para consultas IA
- **Filtros avanzados** por empresa, ubicación y propuesta de valor
- **API REST completa** para integración con otros sistemas

## 🏢 Empresas Incluidas

| Empresa | Modelo de Negocio | Ubicación | Financiación | Empleados |
|---------|-------------------|-----------|--------------|-----------|
| **Tuio** | MGA Digital | Madrid | €16.7M | 150 |
| **Weecover** | Insurance-as-a-Service | Madrid | €4.2M | 80 |
| **Cobee** | Plataforma de Beneficios | Barcelona | €40M | 200 |
| **BDEO** | Tecnología de Siniestros | Madrid | €25M | 120 |
| **Barkibu** | Telemedicina Veterinaria | Madrid | €3.5M | 45 |
| **Insurama** | Seguros Tecnología | Madrid | €8M | 65 |
| **Stoïk** | Ciberseguros | Madrid | €25M | 35 |
| **Life5** | Seguros de Vida Digital | Barcelona | €2M | 25 |
| **Swipet** | Seguros para Mascotas | Valencia | €3M | 40 |
| **Asistensi** | Asistencia Digital | Sevilla | €4.5M | 55 |

**Total:** €131.9M en financiación, 815 empleados

## 🛠️ Tecnologías

### Frontend
- **React 19** con TypeScript
- **Tailwind CSS** para estilos
- **shadcn/ui** para componentes
- **Vite** para desarrollo y build

### Backend
- **Flask** (Python)
- **SQLite** para base de datos
- **LangChain** para agentes IA
- **Flask-CORS** para API

### Deployment
- **Manus Cloud** para hosting
- **Git** para control de versiones

## 🚀 Instalación y Uso

### Prerrequisitos
- Node.js 18+
- Python 3.11+
- pnpm o npm

### 1. Clonar el repositorio
```bash
git clone https://github.com/miguelgonez/insurtech.git
cd insurtech
```

### 2. Configurar Backend
```bash
# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar servidor
python src/main.py
```

### 3. Configurar Frontend (Desarrollo)
```bash
cd insurtech-frontend

# Instalar dependencias
pnpm install

# Ejecutar en desarrollo
pnpm run dev
```

### 4. Acceder a la aplicación
- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:5002

## 📁 Estructura del Proyecto

```
insurtech/
├── src/                          # Backend Flask
│   ├── main.py                   # Servidor principal
│   ├── static/                   # Frontend construido
│   └── routes/                   # Rutas de la API
├── insurtech-frontend/           # Código fuente React
│   ├── src/
│   │   ├── App.tsx              # Componente principal
│   │   ├── components/ui/       # Componentes UI
│   │   └── lib/                 # Utilidades
│   ├── package.json
│   └── vite.config.js
├── insurtech_espana.db          # Base de datos SQLite
├── requirements.txt             # Dependencias Python
├── PROYECTO_COMPLETO.md         # Documentación técnica
├── ENTREGABLES_FINALES.md       # Resumen del proyecto
└── README.md                    # Este archivo
```

## 🎯 Funcionalidades

### ✅ Interfaz Usuario
- **Menú lateral tipo Streamlit** con todas las empresas
- **Filtros desplegables** por empresa, ubicación, tipo de solución
- **Búsqueda en tiempo real**
- **Vista detallada** de cada empresa con campos tipo Crunchbase
- **Responsive design** para desktop y móvil

### ✅ Sistema de Agentes IA
- **Agentes especializados** por empresa
- **Consultas en lenguaje natural**
- **Respuestas detalladas** con análisis especializado
- **Análisis transversal** del ecosistema

### ✅ API REST
- `GET /api/agents/companies` - Listar empresas
- `POST /api/agents/companies/{id}/query` - Consultar agente
- `GET /api/agents/companies/{id}/solutions` - Obtener soluciones
- `POST /api/agents/analysis/{type}` - Análisis transversal

## 🔍 Ejemplos de Uso

### Consultas a Agentes Especializados
```
"¿Cuál es la propuesta de valor de Tuio y cómo se diferencia de sus competidores?"
"¿Qué tecnologías utiliza BDEO para el análisis de siniestros?"
"¿Cuál es el modelo de financiación de Weecover?"
```

### Filtros Disponibles
- **Por empresa:** Selección directa de cualquier empresa
- **Por ubicación:** Madrid, Barcelona, Valencia, Sevilla
- **Por tipo de solución:** MGA Digital, Ciberseguros, Telemedicina, etc.

## 📊 Datos y Métricas

- **10 empresas Insurtech** verificadas y activas
- **Campos tipo Crunchbase:** Financiación, empleados, ubicación, contacto
- **Relaciones 1:n:** Cada empresa puede tener múltiples soluciones
- **Cobertura geográfica:** 4 ciudades principales de España

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

## 👨‍💻 Autor

**Miguel González**
- GitHub: [@miguelgonez](https://github.com/miguelgonez)

## 🙏 Agradecimientos

- Datos recopilados de fuentes públicas del ecosistema Insurtech español
- Inspirado en la necesidad de centralizar información del sector
- Desarrollado con las mejores prácticas de desarrollo web moderno

---

⭐ **¡Dale una estrella si este proyecto te resulta útil!**

