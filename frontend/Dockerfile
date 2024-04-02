# Use official Node.js image as base
FROM node:alpine

# Set working directory
WORKDIR '/app'

# Copy package.json and install dependencies
COPY package.json .

RUN npm install

# Copy the rest of the application code
COPY . .

ENV BROWSER=echo
# Expose port 3000
EXPOSE 3000

# Run the React app
CMD ["npm", "start"]
