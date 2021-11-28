FROM node:16.11-alpine as build

WORKDIR /usr/src/app/frontend

COPY ./frontend/ ./

RUN npm ci

RUN npm run build --prod

FROM nginx:stable-alpine

COPY --from=build /usr/src/app/frontend/build /usr/share/nginx/html

CMD ["nginx", "-g", "daemon off;"]

