FROM node:22-slim AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable
WORKDIR /app
COPY ./ ./

FROM base AS prod-deps
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --prod --frozen-lockfile
RUN pnpm run build

FROM base AS final
COPY --from=prod-deps /app/node_modules /app/node_modules

EXPOSE 3000
CMD [ "pnpm", "run", "preview", "--host", "0.0.0.0", "--port", "3000" ]