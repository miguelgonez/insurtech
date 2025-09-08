import React, { useState, useEffect } from 'react'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Textarea } from '@/components/ui/textarea'
import { Badge } from '@/components/ui/badge'
import { Alert, AlertDescription } from '@/components/ui/alert'
import { Separator } from '@/components/ui/separator'
import { ScrollArea } from '@/components/ui/scroll-area'
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select'
import { 
  Loader2, 
  Building2, 
  BarChart3, 
  Rocket, 
  CheckCircle, 
  AlertCircle,
  Globe,
  MapPin,
  Users,
  DollarSign,
  Calendar,
  Mail,
  Phone,
  ExternalLink
} from 'lucide-react'
import './App.css'

// Tipos TypeScript
interface Company {
  id: number
  nombre_oficial: string
  nombre_comercial?: string
  descripcion_corta?: string
  propuesta_valor?: string
  modelo_negocio: string
  tipo_relacion: string
  sitio_web?: string
  ciudad?: string
  pais?: string
  año_fundacion?: number
  numero_empleados?: number
  financiacion_total?: number
  email?: string
  telefono?: string
  linkedin?: string
  twitter?: string
}

interface Solution {
  id: number
  nombre: string
  descripcion: string
  categoria_insurtech?: string
  tecnologias?: string
}

interface CompanyDetails {
  company: Company
  solutions: Solution[]
}

const API_BASE_URL = '/api/agents'

function App() {
  // Estados
  const [companies, setCompanies] = useState<Company[]>([])
  const [selectedCompany, setSelectedCompany] = useState<Company | null>(null)
  const [companyDetails, setCompanyDetails] = useState<CompanyDetails | null>(null)
  const [loading, setLoading] = useState(true)
  const [detailsLoading, setDetailsLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [searchTerm, setSearchTerm] = useState('')
  const [companyQuestion, setCompanyQuestion] = useState('')
  const [companyResult, setCompanyResult] = useState<any>(null)
  const [companyLoading, setCompanyLoading] = useState(false)
  const [filterCompany, setFilterCompany] = useState('')
  const [filterLocation, setFilterLocation] = useState('')
  const [filterValueProp, setFilterValueProp] = useState('')

  // Cargar empresas
  useEffect(() => {
    const loadCompanies = async () => {
      try {
        setLoading(true)
        const response = await fetch(`${API_BASE_URL}/companies`)
        const data = await response.json()
        
        if (data.success) {
          setCompanies(data.companies)
          if (data.companies.length > 0) {
            setSelectedCompany(data.companies[0])
          }
        } else {
          throw new Error(data.error || 'Error al cargar empresas')
        }
        
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Error desconocido')
      } finally {
        setLoading(false)
      }
    }

    loadCompanies()
  }, [])

  // Cargar detalles de empresa seleccionada
  useEffect(() => {
    if (selectedCompany) {
      loadCompanyDetails(selectedCompany.id)
    }
  }, [selectedCompany])

  const loadCompanyDetails = async (companyId: number) => {
    try {
      setDetailsLoading(true)
      setCompanyResult(null) // Limpiar resultados anteriores
      setCompanyQuestion('') // Limpiar pregunta anterior
      
      // Cargar soluciones específicas de la empresa
      const response = await fetch(`${API_BASE_URL}/companies/${companyId}/solutions`)
      const data = await response.json()
      
      let solutions: Solution[] = []
      if (data.success && data.solutions) {
        solutions = data.solutions
      } else {
        // Soluciones por defecto basadas en el tipo de empresa
        const company = companies.find(c => c.id === companyId)
        if (company) {
          solutions = generateDefaultSolutions(company)
        }
      }
      
      const company = companies.find(c => c.id === companyId)
      if (company) {
        setCompanyDetails({
          company,
          solutions
        })
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error al cargar detalles')
      // En caso de error, usar soluciones por defecto
      const company = companies.find(c => c.id === companyId)
      if (company) {
        setCompanyDetails({
          company,
          solutions: generateDefaultSolutions(company)
        })
      }
    } finally {
      setDetailsLoading(false)
    }
  }

  // Generar soluciones por defecto basadas en el tipo de empresa
  const generateDefaultSolutions = (company: Company): Solution[] => {
    const baseSolutions: { [key: string]: Solution[] } = {
      'MGA Digital': [
        {
          id: 1,
          nombre: 'Plataforma de Seguros Digitales',
          descripcion: 'Plataforma integral para contratación y gestión de seguros',
          categoria_insurtech: 'Digital Platform',
          tecnologias: 'React, Node.js, AI, Machine Learning'
        },
        {
          id: 2,
          nombre: 'App Móvil',
          descripcion: 'Aplicación móvil para gestión completa de pólizas y siniestros',
          categoria_insurtech: 'Mobile App',
          tecnologias: 'React Native, iOS, Android'
        }
      ],
      'Insurance-as-a-Service': [
        {
          id: 1,
          nombre: 'API de Seguros Embebidos',
          descripcion: 'API para integración de seguros en plataformas de e-commerce',
          categoria_insurtech: 'API Platform',
          tecnologias: 'REST API, Microservices, Cloud'
        },
        {
          id: 2,
          nombre: 'Dashboard de Partners',
          descripcion: 'Panel de control para partners y gestión de pólizas embebidas',
          categoria_insurtech: 'Partner Platform',
          tecnologias: 'Vue.js, Python, Analytics'
        }
      ],
      'Plataforma de Beneficios': [
        {
          id: 1,
          nombre: 'Plataforma de Beneficios Empresariales',
          descripcion: 'Plataforma integral para gestión de beneficios sociales empresariales',
          categoria_insurtech: 'HR Platform',
          tecnologias: 'Angular, Java, Microservices'
        }
      ],
      'Tecnología de Siniestros': [
        {
          id: 1,
          nombre: 'Plataforma de IA para Siniestros',
          descripcion: 'Plataforma de IA para análisis automático de siniestros mediante imágenes',
          categoria_insurtech: 'AI Platform',
          tecnologias: 'Computer Vision, Deep Learning, Python'
        }
      ],
      'Telemedicina Veterinaria': [
        {
          id: 1,
          nombre: 'Consulta Veterinaria Online',
          descripcion: 'Plataforma de telemedicina veterinaria con chat y videollamadas',
          categoria_insurtech: 'Telemedicine',
          tecnologias: 'WebRTC, React, Node.js'
        },
        {
          id: 2,
          nombre: 'Seguros para Mascotas',
          descripcion: 'Seguros veterinarios especializados para mascotas',
          categoria_insurtech: 'Pet Insurance',
          tecnologias: 'Insurance Platform, Mobile App'
        }
      ],
      'Seguros Tecnología': [
        {
          id: 1,
          nombre: 'Seguros para Dispositivos',
          descripcion: 'Protección especializada para dispositivos tecnológicos',
          categoria_insurtech: 'Device Insurance',
          tecnologias: 'Digital Platform, IoT Integration'
        }
      ],
      'Ciberseguros': [
        {
          id: 1,
          nombre: 'Plataforma de Ciberseguros',
          descripcion: 'Protección cibernética especializada para pymes',
          categoria_insurtech: 'Cyber Insurance',
          tecnologias: 'Security Analytics, AI, Cloud'
        }
      ],
      'Seguros de Vida Digital': [
        {
          id: 1,
          nombre: 'Plataforma de Seguros de Vida',
          descripcion: 'Seguros de vida con contratación 100% digital',
          categoria_insurtech: 'Life Insurance',
          tecnologias: 'Digital Platform, AI Underwriting'
        }
      ],
      'Seguros para Mascotas': [
        {
          id: 1,
          nombre: 'Seguros Veterinarios',
          descripcion: 'Seguros veterinarios completos con red de clínicas',
          categoria_insurtech: 'Pet Insurance',
          tecnologias: 'Veterinary Network, Mobile App'
        }
      ],
      'Asistencia Digital': [
        {
          id: 1,
          nombre: 'Servicios de Asistencia 24/7',
          descripcion: 'Servicios de asistencia digital con tecnología avanzada',
          categoria_insurtech: 'Digital Assistance',
          tecnologias: 'AI Chatbots, Emergency Response'
        }
      ]
    }

    return baseSolutions[company.modelo_negocio] || [
      {
        id: 1,
        nombre: 'Solución Principal',
        descripcion: `Solución principal de ${company.nombre_oficial}`,
        categoria_insurtech: 'Digital Platform',
        tecnologias: 'Tecnologías modernas'
      }
    ]
  }

  // Consultar agente especializado
  const handleCompanyQuery = async () => {
    if (!selectedCompany || !companyQuestion.trim()) {
      setError('Por favor ingresa una pregunta')
      return
    }

    try {
      setCompanyLoading(true)
      setCompanyResult(null)
      setError(null)

      const response = await fetch(`${API_BASE_URL}/companies/${selectedCompany.id}/query`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ question: companyQuestion })
      })

      const data = await response.json()
      setCompanyResult(data)

    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error de conexión')
    } finally {
      setCompanyLoading(false)
    }
  }

  // Filtrar empresas por búsqueda y filtros
  const filteredCompanies = companies.filter(company => {
    // Filtro por texto de búsqueda
    const matchesSearch = company.nombre_oficial.toLowerCase().includes(searchTerm.toLowerCase()) ||
      company.modelo_negocio.toLowerCase().includes(searchTerm.toLowerCase()) ||
      (company.descripcion_corta && company.descripcion_corta.toLowerCase().includes(searchTerm.toLowerCase()))
    
    // Filtro por empresa específica
    const matchesCompany = !filterCompany || company.nombre_oficial === filterCompany
    
    // Filtro por ubicación
    const matchesLocation = !filterLocation || company.ciudad === filterLocation
    
    // Filtro por propuesta de valor/categoría
    const matchesValueProp = !filterValueProp || 
      (company.modelo_negocio.toLowerCase().includes(filterValueProp.toLowerCase()) ||
       (company.categorias_insurtech && company.categorias_insurtech.toLowerCase().includes(filterValueProp.toLowerCase())))
    
    return matchesSearch && matchesCompany && matchesLocation && matchesValueProp
  })

  // Obtener opciones únicas para los filtros
  const uniqueCompanies = [...new Set(companies.map(c => c.nombre_oficial))].sort()
  const uniqueLocations = [...new Set(companies.map(c => c.ciudad).filter(Boolean))].sort()
  const uniqueValueProps = [
    'MGA Digital',
    'Insurance-as-a-Service', 
    'Plataforma de Beneficios',
    'Tecnología de Siniestros',
    'Telemedicina',
    'Seguros Tecnología',
    'Ciberseguros',
    'Seguros de Vida',
    'Seguros para Mascotas',
    'Asistencia Digital'
  ]

  // Función para limpiar filtros
  const clearFilters = () => {
    setSearchTerm('')
    setFilterCompany('')
    setFilterLocation('')
    setFilterValueProp('')
  }

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <Loader2 className="h-12 w-12 animate-spin mx-auto mb-4 text-blue-600" />
          <p className="text-lg text-gray-600">Cargando sistema Insurtech...</p>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-gray-50 flex">
      {/* Sidebar tipo Streamlit */}
      <div className="w-80 bg-white border-r border-gray-200 flex flex-col">
        {/* Header del sidebar */}
        <div className="p-6 border-b border-gray-200">
          <h1 className="text-xl font-bold text-gray-900 mb-2">
            🤖 Insurtech España
          </h1>
          <p className="text-sm text-gray-600">
            Sistema de Agentes IA
          </p>
        </div>

        {/* Búsqueda y Filtros */}
        <div className="p-4 border-b border-gray-200 space-y-3">
          <Input
            placeholder="Buscar empresas..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full"
          />
          
          {/* Filtro por Empresa */}
          <Select value={filterCompany} onValueChange={setFilterCompany}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Filtrar por empresa" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="">Todas las empresas</SelectItem>
              {uniqueCompanies.map((company) => (
                <SelectItem key={company} value={company}>
                  {company}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          {/* Filtro por Ubicación */}
          <Select value={filterLocation} onValueChange={setFilterLocation}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Filtrar por ubicación" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="">Todas las ubicaciones</SelectItem>
              {uniqueLocations.map((location) => (
                <SelectItem key={location} value={location}>
                  {location}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          {/* Filtro por Propuesta de Valor */}
          <Select value={filterValueProp} onValueChange={setFilterValueProp}>
            <SelectTrigger className="w-full">
              <SelectValue placeholder="Filtrar por tipo de solución" />
            </SelectTrigger>
            <SelectContent>
              <SelectItem value="">Todos los tipos</SelectItem>
              {uniqueValueProps.map((prop) => (
                <SelectItem key={prop} value={prop}>
                  {prop}
                </SelectItem>
              ))}
            </SelectContent>
          </Select>

          {/* Botón para limpiar filtros */}
          {(searchTerm || filterCompany || filterLocation || filterValueProp) && (
            <Button 
              variant="outline" 
              size="sm" 
              onClick={clearFilters}
              className="w-full"
            >
              Limpiar filtros
            </Button>
          )}
        </div>

        {/* Lista de empresas */}
        <ScrollArea className="flex-1">
          <div className="p-4 space-y-2">
            <h3 className="text-sm font-semibold text-gray-700 mb-3">
              Empresas ({filteredCompanies.length})
            </h3>
            {filteredCompanies.map((company) => (
              <Card
                key={company.id}
                className={`cursor-pointer transition-all hover:shadow-md ${
                  selectedCompany?.id === company.id
                    ? 'ring-2 ring-blue-500 bg-blue-50'
                    : 'hover:bg-gray-50'
                }`}
                onClick={() => setSelectedCompany(company)}
              >
                <CardContent className="p-3">
                  <h4 className="font-semibold text-sm mb-1">
                    {company.nombre_oficial}
                  </h4>
                  <div className="space-y-1">
                    <Badge variant="secondary" className="text-xs">
                      {company.modelo_negocio}
                    </Badge>
                    <Badge variant="outline" className="text-xs">
                      {company.tipo_relacion}
                    </Badge>
                  </div>
                  {company.ciudad && (
                    <p className="text-xs text-gray-500 mt-1 flex items-center">
                      <MapPin className="h-3 w-3 mr-1" />
                      {company.ciudad}
                    </p>
                  )}
                </CardContent>
              </Card>
            ))}
          </div>
        </ScrollArea>

        {/* Footer del sidebar */}
        <div className="p-4 border-t border-gray-200">
          <p className="text-xs text-gray-500 text-center">
            Base de datos: {companies.length} empresas
          </p>
        </div>
      </div>

      {/* Contenido principal */}
      <div className="flex-1 flex flex-col">
        {/* Header principal */}
        <div className="bg-white border-b border-gray-200 p-6">
          <div className="flex items-center justify-between">
            <div>
              <h1 className="text-2xl font-bold text-gray-900">
                Sistema de Agentes Insurtech España
              </h1>
              <p className="text-gray-600">
                Análisis inteligente de empresas y mercado con IA especializada
              </p>
            </div>
            <div className="flex space-x-2">
              <Button variant="outline" size="sm">
                <BarChart3 className="h-4 w-4 mr-2" />
                Análisis
              </Button>
              <Button variant="outline" size="sm">
                <Rocket className="h-4 w-4 mr-2" />
                Demo
              </Button>
            </div>
          </div>
        </div>

        {/* Error Alert */}
        {error && (
          <div className="p-6">
            <Alert className="border-red-200 bg-red-50">
              <AlertCircle className="h-4 w-4 text-red-600" />
              <AlertDescription className="text-red-800">
                {error}
              </AlertDescription>
            </Alert>
          </div>
        )}

        {/* Contenido de la empresa seleccionada */}
        <div className="flex-1 p-6">
          {selectedCompany ? (
            <div className="space-y-6">
              {/* Información básica de la empresa */}
              <Card>
                <CardHeader>
                  <div className="flex items-start justify-between">
                    <div>
                      <CardTitle className="text-2xl">
                        {selectedCompany.nombre_oficial}
                      </CardTitle>
                      {selectedCompany.nombre_comercial && (
                        <CardDescription className="text-lg">
                          {selectedCompany.nombre_comercial}
                        </CardDescription>
                      )}
                    </div>
                    {selectedCompany.sitio_web && (
                      <Button variant="outline" size="sm" asChild>
                        <a href={selectedCompany.sitio_web} target="_blank" rel="noopener noreferrer">
                          <ExternalLink className="h-4 w-4 mr-2" />
                          Sitio Web
                        </a>
                      </Button>
                    )}
                  </div>
                </CardHeader>
                <CardContent>
                  {selectedCompany.descripcion_corta && (
                    <p className="text-gray-700 mb-4">
                      {selectedCompany.descripcion_corta}
                    </p>
                  )}
                  
                  {selectedCompany.propuesta_valor && (
                    <div className="mb-4">
                      <h4 className="font-semibold mb-2">Propuesta de Valor:</h4>
                      <p className="text-gray-700">{selectedCompany.propuesta_valor}</p>
                    </div>
                  )}

                  <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                    {/* Modelo de Negocio */}
                    <div className="flex items-center space-x-2">
                      <Building2 className="h-5 w-5 text-blue-600" />
                      <div>
                        <p className="text-sm font-medium">Modelo de Negocio</p>
                        <p className="text-sm text-gray-600">{selectedCompany.modelo_negocio}</p>
                      </div>
                    </div>

                    {/* Tipo de Relación */}
                    <div className="flex items-center space-x-2">
                      <Users className="h-5 w-5 text-green-600" />
                      <div>
                        <p className="text-sm font-medium">Tipo de Relación</p>
                        <p className="text-sm text-gray-600">{selectedCompany.tipo_relacion}</p>
                      </div>
                    </div>

                    {/* Ubicación */}
                    {selectedCompany.ciudad && (
                      <div className="flex items-center space-x-2">
                        <MapPin className="h-5 w-5 text-red-600" />
                        <div>
                          <p className="text-sm font-medium">Ubicación</p>
                          <p className="text-sm text-gray-600">
                            {selectedCompany.ciudad}, {selectedCompany.pais}
                          </p>
                        </div>
                      </div>
                    )}

                    {/* Año de Fundación */}
                    {selectedCompany.año_fundacion && (
                      <div className="flex items-center space-x-2">
                        <Calendar className="h-5 w-5 text-purple-600" />
                        <div>
                          <p className="text-sm font-medium">Fundación</p>
                          <p className="text-sm text-gray-600">{selectedCompany.año_fundacion}</p>
                        </div>
                      </div>
                    )}

                    {/* Empleados */}
                    {selectedCompany.numero_empleados && (
                      <div className="flex items-center space-x-2">
                        <Users className="h-5 w-5 text-orange-600" />
                        <div>
                          <p className="text-sm font-medium">Empleados</p>
                          <p className="text-sm text-gray-600">{selectedCompany.numero_empleados}</p>
                        </div>
                      </div>
                    )}

                    {/* Financiación */}
                    {selectedCompany.financiacion_total && (
                      <div className="flex items-center space-x-2">
                        <DollarSign className="h-5 w-5 text-green-600" />
                        <div>
                          <p className="text-sm font-medium">Financiación</p>
                          <p className="text-sm text-gray-600">
                            €{selectedCompany.financiacion_total.toLocaleString()}
                          </p>
                        </div>
                      </div>
                    )}
                  </div>

                  {/* Contacto */}
                  {(selectedCompany.email || selectedCompany.telefono || selectedCompany.linkedin) && (
                    <>
                      <Separator className="my-4" />
                      <div>
                        <h4 className="font-semibold mb-2">Contacto:</h4>
                        <div className="flex flex-wrap gap-4">
                          {selectedCompany.email && (
                            <div className="flex items-center space-x-2">
                              <Mail className="h-4 w-4 text-gray-500" />
                              <a href={`mailto:${selectedCompany.email}`} className="text-sm text-blue-600 hover:underline">
                                {selectedCompany.email}
                              </a>
                            </div>
                          )}
                          {selectedCompany.telefono && (
                            <div className="flex items-center space-x-2">
                              <Phone className="h-4 w-4 text-gray-500" />
                              <span className="text-sm text-gray-600">{selectedCompany.telefono}</span>
                            </div>
                          )}
                          {selectedCompany.linkedin && (
                            <div className="flex items-center space-x-2">
                              <ExternalLink className="h-4 w-4 text-gray-500" />
                              <a href={selectedCompany.linkedin} target="_blank" rel="noopener noreferrer" className="text-sm text-blue-600 hover:underline">
                                LinkedIn
                              </a>
                            </div>
                          )}
                        </div>
                      </div>
                    </>
                  )}
                </CardContent>
              </Card>

              {/* Soluciones */}
              {companyDetails && companyDetails.solutions.length > 0 && (
                <Card>
                  <CardHeader>
                    <CardTitle>Soluciones ({companyDetails.solutions.length})</CardTitle>
                    <CardDescription>
                      Productos y servicios ofrecidos por la empresa
                    </CardDescription>
                  </CardHeader>
                  <CardContent>
                    <div className="space-y-4">
                      {companyDetails.solutions.map((solution) => (
                        <div key={solution.id} className="border rounded-lg p-4">
                          <h4 className="font-semibold mb-2">{solution.nombre}</h4>
                          <p className="text-gray-700 mb-2">{solution.descripcion}</p>
                          <div className="flex flex-wrap gap-2">
                            {solution.categoria_insurtech && (
                              <Badge variant="secondary">{solution.categoria_insurtech}</Badge>
                            )}
                            {solution.tecnologias && (
                              <Badge variant="outline">{solution.tecnologias}</Badge>
                            )}
                          </div>
                        </div>
                      ))}
                    </div>
                  </CardContent>
                </Card>
              )}

              {/* Consulta al Agente */}
              <Card>
                <CardHeader>
                  <CardTitle>Consultar Agente Especializado</CardTitle>
                  <CardDescription>
                    Realiza preguntas específicas sobre {selectedCompany.nombre_oficial}
                  </CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <Textarea
                      value={companyQuestion}
                      onChange={(e) => setCompanyQuestion(e.target.value)}
                      placeholder={`Ej: ¿Cuál es la propuesta de valor de ${selectedCompany.nombre_oficial} y cómo se diferencia de sus competidores?`}
                      rows={3}
                    />
                    <Button 
                      onClick={handleCompanyQuery}
                      disabled={!companyQuestion.trim() || companyLoading}
                      className="w-full"
                    >
                      {companyLoading ? (
                        <>
                          <Loader2 className="h-4 w-4 mr-2 animate-spin" />
                          Consultando...
                        </>
                      ) : (
                        <>
                          <Building2 className="h-4 w-4 mr-2" />
                          Consultar Agente
                        </>
                      )}
                    </Button>
                  </div>

                  {/* Resultado de la consulta */}
                  {companyResult && (
                    <div className="mt-6">
                      <Card className="bg-gray-50">
                        <CardHeader>
                          <CardTitle className="flex items-center gap-2">
                            {companyResult.success ? (
                              <CheckCircle className="h-5 w-5 text-green-600" />
                            ) : (
                              <AlertCircle className="h-5 w-5 text-red-600" />
                            )}
                            Respuesta del Agente Especializado
                          </CardTitle>
                        </CardHeader>
                        <CardContent>
                          {companyResult.success ? (
                            <div className="space-y-3">
                              <p><strong>Empresa:</strong> {companyResult.empresa}</p>
                              <p><strong>Pregunta:</strong> {companyResult.pregunta}</p>
                              <div>
                                <strong>Respuesta:</strong>
                                <div className="mt-2 whitespace-pre-wrap bg-white p-3 rounded border">
                                  {companyResult.respuesta}
                                </div>
                              </div>
                            </div>
                          ) : (
                            <p className="text-red-600">{companyResult.error}</p>
                          )}
                        </CardContent>
                      </Card>
                    </div>
                  )}
                </CardContent>
              </Card>
            </div>
          ) : (
            <div className="flex items-center justify-center h-64">
              <div className="text-center">
                <Building2 className="h-12 w-12 text-gray-400 mx-auto mb-4" />
                <p className="text-gray-500">Selecciona una empresa del menú lateral</p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}

export default App

