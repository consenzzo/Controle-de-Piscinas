# Dockerfile para Frontend React
FROM node:14

# Set the working directory
WORKDIR /app

# Install dependencies
COPY package.json .
RUN npm install

# Copy the project
COPY . .

# Expose the port for React
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
