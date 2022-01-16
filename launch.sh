export DATABASE_URL=postgresql://USER:PASSWORD@localhost/hypecycle 

export BLINKA_MCP2221="1"
cd backend;
uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8001 --lifespan on