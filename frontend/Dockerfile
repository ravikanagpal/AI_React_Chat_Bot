# Use the official lightweight Alpine-based Nginx image as the base image
FROM nginx:alpine

# Set the working directory inside the container
# Nginx serves files from this directory by default
WORKDIR /usr/share/nginx/html

# Copy all files from the current directory on the host to the working directory in the container
COPY . /usr/share/nginx/html

# Expose port 80 to allow HTTP traffic into the container
EXPOSE 80

# Start Nginx in the foreground (prevent daemon mode) so the container stays alive
CMD ["nginx", "-g", "daemon off;"]