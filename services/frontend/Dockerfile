# Install dependencies only when needed
FROM node:16-alpine AS deps
RUN apk add --no-cache libc6-compat
WORKDIR /app
COPY package-lock.json ./
COPY package.json ./
RUN npm install


RUN npm run build
# Rebuild the source code only when needed
FROM node:16-alpine AS builder

WORKDIR /app

COPY --from=deps /app/node_modules ./node_modules

COPY . .

RUN npm run build

# Production image, copy all the files and run next
FROM node:16-alpine AS runner
WORKDIR /app

ENV NODE_ENV production

RUN addgroup --system --gid 1001 repogroup
RUN adduser --system --uid 1001 repouser

COPY --from=builder /app/public ./public
COPY --from=builder /app/package.json ./package.json


USER repouser

EXPOSE 3000

ENV PORT 3000

CMD ["node", "server.js"]
