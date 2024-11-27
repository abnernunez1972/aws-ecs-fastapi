from fastapi import FastAPI
import logging

# Configurar logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("fastapi-app")

app = FastAPI()

@app.get("/")
async def read_root():
    try:
        # Registrar el intento de conexión
        logger.info("Intentando responder sin conexión a la base de datos RDS...")
        
        # Comentamos la conexión a RDS para pruebas
        # conn = psycopg2.connect(
        #     host="terraform-20241127161625784100000003.clusqqoy2nvb.us-east-1.rds.amazonaws.com",
        #     database="terraform-20241127161625784100000003",
        #     user="pgadmin",
        #     password="password123"
        # )
        # logger.info("Conexión exitosa a la base de datos.")

        # Ejecutar consulta
        # cur = conn.cursor()
        # logger.info("Ejecutando consulta...")
        # cur.execute("SELECT 'Hello from FastAPI and RDS!'")
        # result = cur.fetchone()
        # cur.close()
        # conn.close()

        logger.info("Respuesta exitosa sin base de datos.")
        return {"message": "Hello from FastAPI without RDS!"}
    except Exception as e:
        logger.error(f"Error en la aplicación: {str(e)}")
        return {"error": str(e)}
