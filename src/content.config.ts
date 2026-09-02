import { defineCollection } from 'astro:content';
import { glob } from 'astro/loaders';
import { z } from 'astro/zod';

const posts = defineCollection({
  loader: glob({
    pattern: ['**/index.md', '!_template/**'],
    base: './src/content/posts',
    generateId: ({ entry }) => entry.split('/')[0],
  }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      date: z.coerce.date(),
      summary: z.string().max(200),
      heroImage: image().optional(),
      sponsor: z
        .object({
          name: z.string(),
          url: z.url().optional(),
        })
        .optional(),
      comingSoon: z.boolean().optional(),
    }),
});

const books = defineCollection({
  loader: glob({
    pattern: ['**/index.md', '!_template/**'],
    base: './src/content/books',
    generateId: ({ entry }) => entry.split('/')[0],
  }),
  schema: ({ image }) =>
    z.object({
      title: z.string(),
      date: z.coerce.date(),
      summary: z.string().max(200),
      cover: image(),
      status: z.enum(['finished', 'in-progress']).default('finished'),
    }),
});

export const collections = { posts, books };
