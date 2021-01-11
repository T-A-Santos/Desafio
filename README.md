# Desafio

<h1> Desafio ScoreCredito </h1>

<h2> Dependencias </h2>
  
 <p> Instale PostgreSQL com <code>sudo apt-get install postgresql postgresql-contrib</code></p>
 
 <h2 Dependencias Python </h2> 
 
 <p> instale as dependências do Python com <code> pip install -r requirements.txt</code></p>
 
 <h2> Criando base de dados </h2>
 
 <p> Crie uma base de dados utilizando postgres</p> 
 <p> após a criação da base de dados, crie um arquivo secrets.json com o seguinte conteudo: </p>
 <br/>
 <code> <br/>{
   <br/> "DATABASE_NAME": "database_name",
   <br/> "DATABASE_USER": "myuser",
   <br/> "DATABASE_HOST": "localhost",
   <br/> "DATABASE_PASS": "mypass"
  }
  </code>
  
  <p> Para a criação do banco de dados rode o arquivo <code> launch_migrations.py</code></p>
