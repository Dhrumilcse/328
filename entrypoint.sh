if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $PgSQL_HOST $PgSQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

exec "$@"