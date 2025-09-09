# 🚀 Deployment Guide for FastAPI + React App

## Overview
This guide will help you deploy your FastAPI backend to **Render** and your React frontend to **Netlify** - both completely FREE!

## 📋 Prerequisites
- GitHub account
- Render account (free)
- Netlify account (free)

---     

## 🔧 Backend Deployment (Render)

### Step 1: Prepare Your Repository
1. Push your code to GitHub
2. Make sure your `backend/` folder contains:
   - `main.py`
   - `requirements.txt`
   - `Procfile`
   - `database.py` (updated with environment variables)

### Step 2: Deploy to Render
1. Go to [render.com](https://render.com) and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Select your repository
5. Configure the service:
   - **Name**: `your-app-backend`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

### Step 3: Add PostgreSQL Database
1. In Render dashboard, click "New +" → "PostgreSQL"
2. Configure:
   - **Name**: `your-app-database`
   - **Database**: `telusko` (or your preferred name)
   - **User**: `postgres`
   - **Region**: Choose closest to you
3. Copy the **External Database URL** (you'll need this)

### Step 4: Configure Environment Variables
1. Go to your web service settings
2. Add environment variable:
   - **Key**: `DATABASE_URL`
   - **Value**: Paste the PostgreSQL URL from Step 3

### Step 5: Deploy
1. Click "Create Web Service"
2. Wait for deployment (5-10 minutes)
3. Your API will be available at: `https://your-app-backend.onrender.com`

---

## 🎨 Frontend Deployment (Netlify)

### Step 1: Prepare Frontend
1. Make sure your `frontend/` folder contains:
   - `package.json`
   - `netlify.toml`
   - Updated `src/App.js` with environment variable support

### Step 2: Deploy to Netlify
1. Go to [netlify.com](https://netlify.com) and sign up
2. Click "New site from Git"
3. Connect your GitHub repository
4. Configure build settings:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/build`

### Step 3: Configure Environment Variables
1. Go to Site settings → Environment variables
2. Add:
   - **Key**: `REACT_APP_API_URL`
   - **Value**: `https://your-app-backend.onrender.com` (your Render API URL)

### Step 4: Deploy
1. Click "Deploy site"
2. Wait for build and deployment (2-5 minutes)
3. Your app will be available at: `https://random-name-123456.netlify.app`

---

## 🔄 Update CORS Settings

After both deployments are complete:

1. Go to your Render backend service
2. Update the CORS origins in `main.py`:
   ```python
   allow_origins=[
       "http://localhost:3000",  # Development
       "https://your-netlify-app.netlify.app",  # Your Netlify URL
   ]
   ```
3. Redeploy your backend

---

## 🗄️ Alternative Free Database Options

### Option 1: Supabase (Recommended)
- **Free tier**: 500MB database, 2GB bandwidth
- **Setup**: Create account at [supabase.com](https://supabase.com)
- **Connection**: Use the connection string from Supabase dashboard

### Option 2: Railway
- **Free tier**: $5 credit monthly
- **Setup**: Create account at [railway.app](https://railway.app)
- **Connection**: Deploy PostgreSQL service, get connection string

### Option 3: Neon
- **Free tier**: 3GB storage, 10GB transfer
- **Setup**: Create account at [neon.tech](https://neon.tech)
- **Connection**: Create database, get connection string

---

## 🚨 Important Notes

### Render Free Tier Limitations:
- **750 hours/month** (enough for small projects)
- **Sleeps after 15 minutes** of inactivity
- **Cold start** takes 30-60 seconds

### Netlify Free Tier:
- **100GB bandwidth/month**
- **Unlimited builds**
- **Global CDN**

### Database Considerations:
- **Render PostgreSQL**: Best for simple projects
- **Supabase**: Best for modern apps with real-time features
- **Railway/Neon**: Good alternatives with more storage

---

## 🔧 Troubleshooting

### Common Issues:

1. **CORS Errors**: Make sure your frontend URL is in the CORS origins list
2. **Database Connection**: Verify your DATABASE_URL environment variable
3. **Build Failures**: Check the build logs in Render/Netlify
4. **Cold Starts**: First request after inactivity will be slow (Render limitation)

### Getting Help:
- Check deployment logs in Render/Netlify dashboards
- Verify all environment variables are set correctly
- Test your API endpoints directly using the Render URL

---

## 🎉 You're Done!

Your app is now live and accessible worldwide! 

- **Frontend**: `https://your-app.netlify.app`
- **Backend API**: `https://your-app.onrender.com`
- **Database**: Connected and running

Remember to update your CORS settings with the actual Netlify URL after deployment!
