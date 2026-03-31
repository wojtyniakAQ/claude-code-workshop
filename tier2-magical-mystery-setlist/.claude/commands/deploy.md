Deploy the app to Google Cloud Run.

Steps:
1. Check if a `Procfile` exists in the current directory. If not, create one with: `web: uvicorn app:app --host 0.0.0.0 --port $PORT`
2. Determine a service name by running `whoami` and prefixing it with `workshop-` (e.g. `workshop-alice`)
3. Run: `gcloud run deploy <service-name> --source . --project saige-wojciech-wojtyniak --region us-central1 --allow-unauthenticated`
4. Wait for the deploy to complete
5. When done, print the service URL on its own line so the user can easily copy it. Format it as: `Your app is live at: <URL>`
