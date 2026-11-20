import { Route, Routes, Link } from 'react-router-dom';
import { lazy, Suspense } from 'react';
import { Layout } from './components/Layout';
import { Home } from './pages/Home';
const LearnIndex = lazy(() => import('./pages/LearnIndex').then((m) => ({ default: m.LearnIndex })));
const Lesson = lazy(() => import('./pages/Lesson').then((m) => ({ default: m.Lesson })));
const Formulas = lazy(() => import('./pages/Formulas').then((m) => ({ default: m.Formulas })));
const Practice = lazy(() => import('./pages/Practice').then((m) => ({ default: m.Practice })));
const Drill = lazy(() => import('./pages/Drill').then((m) => ({ default: m.Drill })));
const MockHome = lazy(() => import('./pages/MockHome').then((m) => ({ default: m.MockHome })));
const MockRun = lazy(() => import('./pages/MockRun').then((m) => ({ default: m.MockRun })));
const MockResult = lazy(() => import('./pages/MockResult').then((m) => ({ default: m.MockResult })));
const Mistakes = lazy(() => import('./pages/Mistakes').then((m) => ({ default: m.Mistakes })));
const Plan = lazy(() => import('./pages/Plan').then((m) => ({ default: m.Plan })));
const Tutor = lazy(() => import('./pages/Tutor').then((m) => ({ default: m.Tutor })));
const Resources = lazy(() => import('./pages/Resources').then((m) => ({ default: m.Resources })));
const ChemData = lazy(() => import('./pages/ChemData').then((m) => ({ default: m.ChemData })));
const Chinese = lazy(() => import('./pages/Chinese').then((m) => ({ default: m.Chinese })));
const Settings = lazy(() => import('./pages/Settings').then((m) => ({ default: m.Settings })));


export function App() {
  return (
    <Layout>
      <Suspense fallback={<p className="muted">Loading…</p>}>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/learn" element={<LearnIndex />} />
        <Route path="/learn/:subject/:subtopic" element={<Lesson />} />
        <Route path="/formulas" element={<Formulas />} />
        <Route path="/formulas/:subject" element={<Formulas />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="/drill" element={<Drill />} />
        <Route path="/mock" element={<MockHome />} />
        <Route path="/mock/run" element={<MockRun />} />
        <Route path="/mock/result/:id" element={<MockResult />} />
        <Route path="/mistakes" element={<Mistakes />} />
        <Route path="/plan" element={<Plan />} />
        <Route path="/tutor" element={<Tutor />} />
        <Route path="/resources" element={<Resources />} />
        <Route path="/chemistry-data" element={<ChemData />} />
        <Route path="/chinese" element={<Chinese />} />
        <Route path="/settings" element={<Settings />} />
        <Route
          path="*"
          element={
            <div className="card">
              <h1>Page not found</h1>
              <Link to="/">Back to the dashboard</Link>
            </div>
          }
        />
      </Routes>
      </Suspense>
    </Layout>
  );
}
